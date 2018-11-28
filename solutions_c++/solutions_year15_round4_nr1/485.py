// * template
#include <bits/stdc++.h>

#ifdef LOCAL
#include "dump.hpp"
#else
#define dump(...)
#endif

using namespace std;


template<class T, class U> inline void fill_array(T &e, const U &v) { e = v; }
template<class T, class U, size_t s> inline void fill_array(T (&a)[s], const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U, size_t s> inline void fill_array(array<T, s> &a, const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U> inline void fill_array(vector<T> &a, const U &v) {for(auto&e:a)fill_array(e,v);}

template<class T> inline void chmin(T &a, const T &b) { if(a > b) a = b; }
template<class T> inline void chmax(T &a, const T &b) { if(a < b) a = b; }

struct range {
	typedef int Int;
	struct iter {
		Int i;
		const Int s;
		iter(const Int &i_, const Int &s_):i(i_), s(s_) {}
		bool operator!=(const iter &r) const { return s > 0 ? i < r.i : i > r.i; }
		const Int &operator*() const { return i; }
		iter &operator++() { i += s; return *this; }
	};
	const Int f, l, s;
	range(const Int &f_, const Int &l_, const Int &s_):f(f_), l(l_), s(s_) {}
	range(const Int &f_, const Int &l_):f(f_), l(l_), s(1) {}
	range(const Int &num):f(0), l(num), s(1) {}
	iter begin() const { return iter(f, s); }
	iter end() const { return iter(l, s); }
};

// * solve

constexpr int dx[] = {1, 0, -1, 0};
constexpr int dy[] = {0, 1, 0, -1};
const map<char, int> dir{{'>', 0}, {'v', 1}, {'<', 2}, {'^', 3}};

class solver {
private:
	int r, c;
	vector<string> field;

	void init() {
	}

public:
	void input() {
		init();
		cin >> r >> c;
		field.resize(r);
		for(auto &e : field) cin >> e;
	}

	bool search(int x, int y, int d) {
		while(true) {
			x += dx[d];
			y += dy[d];
			if(x < 0 || y < 0 || x >= c || y >= r) return false;
			if(field[y][x] != '.') return true;

		}
	}

	string solve() {
		int ans = 0;
		for(int y : range(r)) {
			for(int x : range(c)) {
				if(field[y][x] != '.') {
					const int def_dir = dir.at(field[y][x]);

					int cost = INT_MAX;

					for(int d = 0; d < 4; ++d) {
						if(search(x, y, d)) {
							chmin(cost, (d == def_dir ? 0 : 1));
						}
					}

					if(cost == INT_MAX) return "IMPOSSIBLE";
					ans += cost;
				}
			}
		}

		return to_string(ans);
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
	vector<decltype(solver::solve()> ans(T);

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
		cout << "Case #" << t << ": " << ans[t - 1] << '\n';
	}

#else
	solver s;
	for(int t = 1; t <= T; ++t) {
		s.input();
		const auto ans = s.solve();
		cout << "Case #" << t << ": " << ans << '\n';
	}
#endif

	return EXIT_SUCCESS;
}
