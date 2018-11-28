#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forr(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define fornr(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forrr(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define printvec(v) for (auto e : v) cout << e << ", "; cout << endl;
#define all(x) (x).begin(), (x).end()

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

struct MaxFlow {
	struct Edge {
		int from;
		int to;
		int flow;
		int capacity;
		Edge *reverse;
		Edge(int from, int to, int flow, int capacity)
			: from(from), to(to), flow(flow), capacity(capacity) {}
		void print() {
			cerr << from << " -> " << to << ' ' << flow << " of " << capacity << endl;
		}
	};
	vector<list<Edge>> edges;
	vector<int> levels;
	vector<list<Edge>::iterator> bookmark;
	int N;
	MaxFlow(int n) {
		N = n;
		edges = vector<list<Edge>>(n);
		levels = vector<int>(n);
		bookmark = vector<list<Edge>::iterator>(n);
	}

	void print() {
		for (auto es : edges) {
			for (auto e : es) {
				e.print();
			}
		}
	}

	void add_edge(int from, int to, int flow, int capacity) {
		edges[from].push_back(Edge(from, to, flow, capacity));
		edges[to].push_back(Edge(to, from, flow, 0));
		edges[from].back().reverse = &(edges[to].back());
		edges[to].back().reverse = &(edges[from].back());
	}

	bool bfs(int source, int target) {
		for (int i = 0; i < N; ++i) {
			levels[i] = INT_MAX;
			bookmark[i] = edges[i].begin();//edges[i].size()-1;
		}
		levels[source] = 0;
		queue<int> q;
		q.push(source);
		while (q.size() > 0) {
			int current = q.front(); q.pop();
			if (current == target) return true;
			int level = levels[current] + 1;
			for (auto edge : edges[current]) {
				if (edge.capacity - edge.flow > 0 && level < levels[edge.to]) {
					levels[edge.to] = level;
					q.push(edge.to);
				}
			}
		}
		return false;
	}

	int dfs(int current, int target, int min_cap) {
		if (current == target) return min_cap;
		int res = 0;
		int level = levels[current]+1;
		//for (int i = bookmark[current]; i >= 0; bookmark[current] = --i) {
		for (auto e = bookmark[current]; min_cap > 0 && e != edges[current].end(); bookmark[current] = ++e) {
			Edge& edge = *e;
			if (level != levels[edge.to] || edge.flow == edge.capacity) continue;
			int add = dfs(edge.to, target, min(min_cap, edge.capacity - edge.flow));
			if (add == 0) continue;
			res += add;
			edge.flow += add;
			edge.reverse->flow -= add;
			min_cap -= add;
		}
		return res;
	}

	int run(int source, int target) {
		int flow = 0;
		while (bfs(source, target)) {
			int add = 0;
			while (0 < (add = dfs(source, target, INT_MAX))) {
				flow += add;
			}
		}
		return flow;
	}
};

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        int N;
        cin >> N;
        vector<string> first(N);
        vector<string> second(N);
        map<string, int> fcnts;
        map<string, int> scnts;
        forn(i, N) {
            cin >> first[i] >> second[i];
            fcnts[first[i]]++;
            scnts[second[i]]++;
        }
        int real = 0;
        set<string> f;
        set<string> s;
        forn(i, N) {
            if (fcnts[first[i]] == 1 || scnts[second[i]] == 1) {
                f.insert(first[i]);
                s.insert(second[i]);
                ++real;
            }
        }
        map<string, int> fn;
        map<string, int> sn;
        forn(i, N) {
            if (f.count(first[i]) == 0 && fn.count(first[i]) == 0) {
                int index = fn.size();
                fn[first[i]] = index;
            }
            if (s.count(second[i]) == 0 && sn.count(second[i]) == 0) {
                int index = sn.size();
                sn[second[i]] = index;
            }
        }
        const int NCNT = fn.size() + sn.size() + 2;
		MaxFlow maxFlow(NCNT);
        for (auto p : fn) {
            maxFlow.add_edge(NCNT-2, p.second, 0, 1);
        }
        for (auto p : sn) {
            maxFlow.add_edge(p.second + fn.size(), NCNT-1, 0, 1);
        }

        forn(i, N) {
            if (f.count(first[i]) == 0 && s.count(second[i]) == 0) {
                maxFlow.add_edge(fn[first[i]], sn[second[i]] + fn.size(), 0, 1);
            }
        }
        int m = maxFlow.run(NCNT-2, NCNT-1);


        /* cout << N << ' ' << real << ' ' << m << ' ' << fn.size() << ' ' << sn.size() << endl; */
        cout << "Case #" << casenum << ": " << (N - real + m - fn.size() - sn.size()) << endl;
    }
    return 0;
}

