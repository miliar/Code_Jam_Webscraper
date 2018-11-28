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

const string kind = "RPS";
class solver {
private:
	int n;
	int num;
	array<int, 3> P;
	const string Z = "Z";

	void init() {
	}

	string check(const int round, const int winner) {
		if(round == 0) {
			if(--P[winner] < 0) return Z;
			return string(1, kind[winner]);
		}
		const int loser = (winner + 2) % 3;
		const string l = check(round - 1, winner);
		const string r = check(round - 1, loser);

		if(l == Z || r == Z) return Z;
		return min(l, r) + max(l, r);
	}

public:
	void input() {
		init();
		cin >> n >> P[0] >> P[1] >> P[2];
		num = accumulate(begin(P), end(P), 0);
	}

	string solve() {
		string res = Z;
		for(int i = 0; i < 3; ++i) {
			const auto tmp = P;
			chmin(res, check(n, i));
			P = tmp;
		}
		if(res == Z) return "IMPOSSIBLE";
		return res;
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
