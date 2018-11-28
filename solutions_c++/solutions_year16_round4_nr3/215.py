// * template
#include <bits/stdc++.h>

#ifdef LOCAL
#include "dump.hpp"
#else
#define dump(...)
#endif

using namespace std;

template<class T> inline void chmax(T &a, const T &b) { if(a < b) a = b; }
template<class T> inline void chmin(T &a, const T &b) { if(a > b) a = b; }

template<class T, class U> inline void fill_array(T &e, const U &v) { e = v; }
template<class T, class U, size_t s> inline void fill_array(T (&a)[s], const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U, size_t s> inline void fill_array(array<T, s> &a, const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U> inline void fill_array(vector<T> &a, const U &v) {for(auto&e:a)fill_array(e,v);}

// * solve

class solver {
private:
	using Graph = vector<vector<int>>;
	int num;
	int r, c;
	vector<pair<int, int>> P;
	int V;
	int out;

	int index(const int x, const int y) {
		return y * c + x;
	}

	int offset(const int x, const int y) {
		return 4 * index(x, y) + out;
	}

	void init() {
	}

	bool check(const Graph &G) {
		int count = 0;
		vector<int> label(V, -1);

		for(int i = 0; i < out; ++i) {
			if(label[i] == -1) {
				const int id = count++;
				if(count > num) return false;

				label[i] = id;
				queue<int> que;
				que.emplace(i);
				while(!que.empty()) {
					const int v = que.front();
					que.pop();

					for(const auto &u : G[v]) {
						if(label[u] == -1) {
							label[u] = id;
							que.emplace(u);
						}
					}
				}
			}
		}

		set<int> used;
		for(const auto &e : P) {
			if(used.count(e.first) || label[e.first] != label[e.second]) return false;
			used.emplace(e.first);
		}
		return true;
	}

public:
	void input() {
		init();
		cin >> r >> c;
		num = r + c;
		P.clear();
		for(int i = 0; i < num; ++i) {
			int a, b;
			cin >> a >> b;
			P.emplace_back(a - 1, b - 1);
		}
		out = 2 * num;
		V = out + 4 * r * c;
	}

	string solve() {
		for(int bit = 0; bit < (1 << (r * c)); ++bit) {
			Graph G(V);
			const auto add_edge = [&](const int a, const int b) {
				assert(0 <= a && a < V);
				assert(0 <= b && b < V);
				G[a].emplace_back(b);
				G[b].emplace_back(a);
			};

			for(int i = 0; i < out; ++i) {
				if(i < c) {
					add_edge(i, 0 + offset(i, 0));
				}
				else if(i < r + c) {
					add_edge(i, 1 + offset(c - 1, (i - c)));
				}
				else if(i < r + c + c) {
					add_edge(i, 2 + offset(c - 1 - (i - (r + c)), r - 1));
				}
				else {
					add_edge(i, 3 + offset(0, r - 1 - (i - (r + c + c))));
				}
			}

			ostringstream oss;
			for(int i = 0; i < r; ++i) {
				for(int j = 0; j < c; ++j) {
					const int o = offset(j, i);
					if(bit & (1 << index(j, i))) {
						add_edge(0 + o, 1 + o);
						add_edge(2 + o, 3 + o);
						oss << '\\';
					}
					else {
						add_edge(0 + o, 3 + o);
						add_edge(1 + o, 2 + o);
						oss << '/';
					}

					if(i > 0) {
						const int o2 = offset(j, i - 1);
						add_edge(0 + o, 2 + o2);
					}
					if(j > 0) {
						const int o2 = offset(j - 1, i);
						add_edge(3 + o, 1 + o2);
					}
				}
				oss << '\n';
			}

			if(check(G)) return oss.str();
		}
		return "IMPOSSIBLE\n";
	}
};

// * main

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

#ifdef _OPENMP
	int next_index = 0;
	vector<decltype(solver().solve())> ans(T);

	#pragma omp parallel for
	for(int t = 0; t < T; ++t) {
		int index;
		solver s;

		#pragma omp critical
		{
			index = next_index++;
			s.input();
		}

		ans[index] = s.solve();
	}

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":\n" << ans[t - 1];
	}

#else
	solver s;
	for(int t = 1; t <= T; ++t) {
		s.input();
		const auto ans = s.solve();
		cout << "Case #" << t << ":\n" << ans;
	}
#endif

	return EXIT_SUCCESS;
}
