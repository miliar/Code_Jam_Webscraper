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
	typedef bitset<2200> Bitset;

	int n;
	//string english, french;
	//vector<string> unknown;
	Bitset english, french;
	vector<Bitset> unknown;
	map<string, int> index;
	int ans;

	void init() {
		index.clear();
	}

	void convert(Bitset &bit) {
		string line;
		getline(cin, line);
		istringstream iss(line);

		bit.reset();
		for(string in; iss >> in;) {
			if(!index.count(in)) index.emplace(in, index.size());
			bit.set(index[in]);
		}
	}

	void dfs(int idx, const Bitset &en, const Bitset &fr) {
		const int common = (en & fr).count();
		if(common >= ans) return;
		if(idx == n) {
			ans = common;
			return;
		}

		dfs(idx + 1, en | unknown[idx], fr);
		dfs(idx + 1, en, fr | unknown[idx]);
	}

public:
	void input() {
		init();
		cin >> n;
		n -= 2;
		cin.ignore();
		convert(english);
		convert(french);
		unknown.resize(n);
		for(auto &e : unknown) convert(e);
	}

	int solve() {
		ans = 2300;
		dfs(0, english, french);
		return ans;
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
