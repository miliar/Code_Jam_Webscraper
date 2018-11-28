#include <bits/stdc++.h>

using namespace std;

const long SRC = 0;
const long DST = 1;
const long INF = 0x3f3f3f3f3f3f3f3fL;

unordered_map<long, long> bucket;

inline long H(const string &s) {
	long ret = 0;
	for(const auto &ch : s) {
		ret = (ret << 5) | (ch - 'a' + 1);
	}
	return ret;
}

long ptr = 0;

inline long ID(const string &s) {
	auto h = H(s);
	auto it = bucket.find(h);
	if (it == bucket.end()) {
		bucket[h] = ptr;
		return ptr;
	} else {
		return it->second;
	}
}

struct Edge {
	long to, f;
	Edge *rev;
	Edge() {}
	Edge(const long &t, const long &f) : to(t), f(f) {}
};

Edge _e[1048576];
Edge *now;
vector<Edge*> e[16384];
long label[16384];
long cur[16384];
queue<long> Q;

inline void addEdge(const long &from, const long &to, const long &f) {
	Edge *a = now++;
	Edge *b = now++;
	a->to = to;
	a->f = f;
	a->rev = b;
	b->to = from;
	b->f = 0;
	b->rev = a;
	e[from].push_back(a);
	e[to].push_back(b);
}

bool relabel() {
	memset(label, -1, sizeof label);
	label[SRC] = 0;
	while(Q.size()) Q.pop();
	Q.push(SRC);
	while(Q.size()) {
		long now = Q.front();
		Q.pop();
		for(const auto &next : e[now]) {
			const auto &to = next->to;
			if (label[to] == -1 && next->f > 0) {
				label[to] = label[now] + 1;
				Q.push(to);
			}
		}
	}
	return label[DST] != -1;
}

long flow(const long &now, const long &f) {
	if (now == DST) return f;
	auto &idx = cur[now];
	long ansf = 0;
	long leftf = f;
	for(; idx < e[now].size(); ++ idx) {
		const auto &next = e[now][idx];
		if(label[next->to] == label[now] + 1) {
			if (next->f > 0) {
				long curf = flow(next->to, min(next->f, leftf));
				leftf -= curf; ansf += curf;
				next->f -= curf; next->rev->f += curf;
				if (leftf == 0) break;
			}
		}
	}
	return ansf;
}

inline long dinic() {
	long ret = 0;
	while(relabel()) {
		memset(cur, 0, sizeof cur);
		ret += flow(SRC, INF);
	}
	return ret;
}

int main(void) {
	ios::sync_with_stdio(false);
	bucket.rehash(99991);
	long T;
	cin >> T;
	for(long t = 1; t <= T; ++ t) {
		bucket.clear(); ptr = 0; now = _e;
		register long i, j;
		for(i = 0; i < 16384; ++ i) e[i].clear();
		long n;
		cin >> n;
		string s;
		s.reserve(16384);
		getline(cin, s);
		for(i = 0; i < n; ++ i) {
			getline(cin, s);
			stringstream tokenizer(s);
			string token;
			token.reserve(32);
			while((tokenizer >> token) && token.length() && token[0] >= 'a' && token[0] <= 'z') {
				auto id = ID(token);
				if (id == ptr) {
					addEdge(n + id * 2, n + id * 2 + 1, 1);
					++ ptr;
				}
				if (i == 0) {
					addEdge(0, n + id * 2, INF);
				} else if (i == 1) {
					addEdge(n + id * 2 + 1, 1, INF);
				} else {
					addEdge(i, n + id * 2, INF);
					addEdge(n + id * 2 + 1, i, INF);
				}
			}
		}
		cout << "Case #" << t << ": " << dinic() << endl;
	}
}
