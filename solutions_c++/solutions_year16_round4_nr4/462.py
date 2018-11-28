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

constexpr int MAX_N = 4;
class solver {
private:
	using Bit = bitset<MAX_N>;
	int n;
	vector<Bit> mat;
	void init() {
		mat.clear();
	}

	bool dfs(Bit &human, Bit &machine) {
		if(human.none()) return true;

		for(int i = 0; i < n; ++i) {
			if(!human[i]) continue;
			if((mat[i] & machine).none()) return false;
			human[i] = false;
			for(int j = 0; j < n; ++j) {
				if(mat[i][j] && machine[j]) {
					machine[j] = false;
					if(!dfs(human, machine)) return false;
					machine[j] = true;
				}
			}
			human[i] = true;
		}
		return true;
	}

	bool check() {
		Bit human((1 << n) - 1), machine((1 << n) - 1);
		return dfs(human, machine);
	}

public:
	void input() {
		init();
		cin >> n;
		for(int i = 0; i < n; ++i) {
			Bit b;
			cin >> b;
			mat.emplace_back(b);
		}
	}

	int solve() {
		int ans = INT_MAX;
		for(int bit = 0; bit < (1 << n * n); ++bit) {
			const int num = __builtin_popcount(bit);
			if(ans <= num) continue;
			auto tmp = mat;
			for(int i = 0; i < n; ++i) {
				for(int j = 0; j < n; ++j) {
					const int id = 1 << (i * n + j);
					if(bit & id) {
						if(mat[i][j]) goto next;
						mat[i][j] = true;
					}
				}
			}

			if(check()) ans = num;
		next:;
			mat = tmp;
		}
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
