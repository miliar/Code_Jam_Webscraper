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
	using Real = long double;
	int n, k;
	vector<Real> P;

	void init() {
	}

public:
	void input() {
		init();
		cin >> n >> k;
		P.resize(n);
		for(auto &e : P) cin >> e;
	}

	Real solve() {
		sort(begin(P), end(P));
		Real res = 0;
		for(int bit = 0; bit < (1 << n); ++bit) {
			if(__builtin_popcount(bit) != k) continue;

			Real tmp = 0.0;
			for(int yes = 0; yes < (1 << n); ++yes) {
				if(__builtin_popcount(yes) != k / 2 || (yes & bit) != yes) continue;
				Real p = 1.0;
				for(int i = 0; i < n; ++i) {
					const int id = 1 << i;
					if(id & bit) {
						if(id & yes) {
							p *= P[i];
						}
						else {
							p *= 1 - P[i];
						}
					}
				}
				tmp += p;
			}
			chmax(res, tmp);
		}
		return res;
	}
};

// * main

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
	cout.setf(ios::fixed);
	cout.precision(10);

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
