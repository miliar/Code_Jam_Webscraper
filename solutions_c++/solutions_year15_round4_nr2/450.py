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

class solver {
private:
	typedef long double Real;

	int n;
	Real v, x;
	vector<Real> r, c;
	void init() {
	}

public:
	void output() {
		dump(n, v, x);
		dump(r, c);
	}

	void input() {
		init();
		cin >> n >> v >> x;
		r.resize(n);
		c.resize(n);
		for(int i : range(n)) {
			cin >> r[i] >> c[i];
		}
	}

	string d2s(Real d) {
		ostringstream oss;
		oss.setf(ios::fixed);
		oss.precision(10);
		oss << d;
		return oss.str();
	}

	string solve() {
		if(n == 1 || (n == 2 && c[0] == c[1])) {
			if(c[0] == x) {
				const Real rt = (n == 1 ? r[0] : r[0] + r[1]);
				return d2s(v / rt);
			}
			else {
				return "IMPOSSIBLE";
			}
		}

		if(n == 2) {
			if(x > max(c[0], c[1]) || x < min(c[0], c[1])) return "IMPOSSIBLE";
			const Real v1 = v * (x - c[0]) / (c[1] - c[0]);
			const Real v0 = v - v1;
			const Real t1 = v1 / r[1];
			const Real t0 = v0 / r[0];
			const Real ans = max(t1, t0);
			assert(t0 >= -1e-10 && t1 >= -1e-10);
			if(ans <= 1e-10) return "IMPOSSIBLE";
			return d2s(ans);
		}

		assert(false);
		return "IMPOSSIBLE";
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
		//s.output();
		cout << "Case #" << t << ": " << ans << '\n';
	}
#endif

	return EXIT_SUCCESS;
}
