#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <cassert>

using std::map;
using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;
using std::string;
using std::istringstream;
using std::min;
using std::max;

const int N = 11111111;

const int INF = INT_MAX;

class Bank {
	map<string, int> words;
	public:
	int get_no(string word) {
		int c = words.count(word);
		if (c == 0) {
			words[word] = words.size();
		}
		return words[word];
	}
	void reset(void) {
		words.clear();
	}
} bank;

int tail, ptr[N];
struct edge_t {
	int u, v;
	int c;
	int next;
	edge_t() {}
	edge_t(int u, int v, int c, int next) : u(u), v(v), c(c), next(next) {}
} edges[N];

void insert(int u, int v, int c) {
	edges[tail] = edge_t(u, v, c, ptr[u]);
	ptr[u] = tail ++;
	edges[tail] = edge_t(v, u, 0, ptr[v]);
	ptr[v] = tail ++;

	assert(tail < N);

	// cout << u << ' ' << v << ' ' << c << endl;
}

int q[N], d[N];

vector<string> split(string sentence) {
	vector<string> words;
	istringstream iss(sentence);
	while (iss) {
		string word;
		iss >> word;
		if (word.size() == 0) break;
		words.push_back(word);
	}
	return words;
}

bool build(int s, int t) {
	memset(d, 0, sizeof(d));
	int head = 0, tail = 1;
	q[0] = s;
	d[s] = 1;
	while (head < tail) {
		int u = q[head++];
		assert(head < N);
		for (int i = ptr[u]; i >= 0; i = edges[i].next) {
			int v = edges[i].v;
			if (edges[i].c > 0 && d[v] == 0) {
				q[tail++] = v;
				assert(tail < N);
				d[v] = d[u] + 1;
			}
		}
	}
	return d[t] > 0;
}

int dinic(int u, int t, int flow) {
	if (u == t) return flow;
	int ret = 0;
	for (int i = ptr[u]; i >= 0; i = edges[i].next) {
		int v = edges[i].v;
		if (edges[i].c > 0 && d[u] + 1 == d[v]) {
			int r = dinic(v, t, min(edges[i].c, flow));
			edges[i].c -= r;
			edges[i ^ 1].c += r;
			flow -= r;
			ret += r;
			if (flow == 0) return ret;
		}
	}
	d[u] = -1;
	return ret;
}

int solve() {
	tail = 0;
	memset(ptr, -1, sizeof(ptr));
	bank.reset();

	int n, V;
	string str;
	cin >> n;
	V = n;
	getline(cin, str);
	for (int _ = 0; _ < n; ++ _) {
		getline(cin, str);
		vector<string> words = split(str);
		for (size_t i = 0; i < words.size(); ++ i) {
			string word = words[i];
			int no = bank.get_no(word);
			if (n + no * 2 >= V) {
				insert(n + no * 2, n + no * 2 + 1, 1);
				V += 2;
			}
			if (_ == 0) {
				insert(0, n + no * 2, INF);
			} else if (_ == 1) {
				insert(n + no * 2 + 1, _, INF);
			} else {
				insert(_, n + no * 2, INF);
				insert(n + no * 2 + 1, _, INF);
			}
		}
	}

	int result = 0;
	while (build(0, 1)) {
		result += dinic(0, 1, INF);
	}
	return result;
}

int main() {
	int test_count;
	cin >> test_count;
	for (int test = 1; test <= test_count; ++ test) {
		cout << "Case #" << test << ": ";// << endl;
		cout << solve() << endl;
	}
	return 0;
}
