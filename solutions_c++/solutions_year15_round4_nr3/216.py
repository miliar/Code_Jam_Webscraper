#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

template<class Flow>
struct Maxflow {
	static const Flow INF = ~0U >> 1; //should change with type
//	static const Flow INF = numeric_limits<Flow>::max();
	struct Edge {
		int t;
		Flow c;
		Edge*n, *r;
		Edge(int _t, Flow _c, Edge*_n) :
				t(_t), c(_c), n(_n) {
		}
	};
	vector<Edge*> E;

	int addV() {
		E.push_back((Edge*) 0);
		return E.size() - 1;
	}

	void clear() {
		E.clear();
	}

	Edge* makeEdge(int s, int t, Flow c) {
		return E[s] = new Edge(t, c, E[s]);
	}

	void addEdge(int s, int t, Flow c) {
		Edge*e1 = makeEdge(s, t, c), *e2 = makeEdge(t, s, 0);
		e1->r = e2, e2->r = e1;
	}

	int calcMaxFlow(int vs, int vt) {
		int nV = E.size();
		Flow totalFlow = 0;

		vector<Flow> am(nV, 0);
		vector<int> h(nV, 0), cnt(nV + 1, 0);
		vector<Edge*> prev(nV, (Edge*) 0), cur(nV, (Edge*) 0);
		cnt[0] = nV;

		int u = vs;
		Edge*e;
		am[u] = INF;
		while (h[vs] < nV) {
			for (e = cur[u]; e; e = e->n)
				if (e->c > 0 && h[u] == h[e->t] + 1)
					break;
			if (e) {
				int v = e->t;
				cur[u] = prev[v] = e;
				am[v] = min(am[u], e->c);
				u = v;
				if (u == vt) {
					Flow by = am[u];
					while (u != vs) {
						prev[u]->c -= by;
						prev[u]->r->c += by;
						u = prev[u]->r->t;
					}
					totalFlow += by;
					am[u] = INF;
				}
			} else {
				if (!--cnt[h[u]])
					break;
				h[u] = nV;
				for (e = E[u]; e; e = e->n)
					if (e->c > 0 && h[e->t] + 1 < h[u]) {
						h[u] = h[e->t] + 1;
						cur[u] = e;
					}
				++cnt[h[u]];
				if (u != vs)
					u = prev[u]->r->t;
			}
		}

		return totalFlow;
	}

	~Maxflow() {
		for (int i = 0; i < E.size(); ++i) {
			for (Edge*e = E[i]; e;) {
				Edge*ne = e->n;
				delete e;
				e = ne;
			}
		}
	}
};

vector<string> split(string s, string del = " ") {
	vector<string> ret;
	s += del[0];

	string w = "";

	for (int i = 0; i < s.size(); ++i) {
		if (del.find(s[i]) == string::npos) {
			w += s[i];
		} else {
			if (w != "")
				ret.push_back(w);
			w = "";
		}
	}

	return ret;
}

vector<string> read_words() {
	static char buf[100000];
	scanf(" ");
	gets(buf);
	return split(buf);
}

map<string, int> word_id;

int get_id(string s) {
	if (word_id.count(s))
		return word_id[s];
	int me = word_id.size();
	return word_id[s] = me;
}

const int BIG = int(1e8);

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		int n;
		cin >> n;
		vector<string> sent[300];

		word_id.clear();
		for (int i = 0; i < n; ++i) {
			sent[i] = read_words();
//			cout << sent[i].size() << endl;
			for (int j = 0; j < sent[i].size(); ++j) {
				get_id(sent[i][j]);
			}
		}

		vector<vector<int> > in(word_id.size(), vector<int>());

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < sent[i].size(); ++j) {
				in[get_id(sent[i][j])].push_back(i);
			}
		}

		Maxflow<int> net;

		//0:must be white
		//1:must be black
		//W_i: lost of being white, B_i lost of being black
		int W[300], B[300];
		memset(W, 0, sizeof W);
		memset(B, 0, sizeof B);
		B[0] = BIG;
		W[1] = BIG;

		int sent_v[300];
		for (int i = 0; i < n; ++i) {
			sent_v[i] = net.addV();
		}
		int vs = net.addV();
		int vt = net.addV();
		for (int i = 0; i < n; ++i) {
			net.addEdge(vs, sent_v[i], B[i]);
			net.addEdge(sent_v[i], vt, W[i]);
		}

		for (int i = 0; i < word_id.size(); ++i) {
			int v = net.addV();
			net.addEdge(vs, v, 1);
			for (vector<int>::iterator j = in[i].begin(); j != in[i].end();
					++j) {
				net.addEdge(v, sent_v[*j], BIG);
			}
			v = net.addV();
			net.addEdge(v, vt, 1);
			for (vector<int>::iterator j = in[i].begin(); j != in[i].end();
					++j) {
				net.addEdge(sent_v[*j], v, BIG);
			}
		}

		int ans = net.calcMaxFlow(vs, vt);
		printf("Case #%d: %d\n", nc, ans - int(word_id.size()));
	}
}
