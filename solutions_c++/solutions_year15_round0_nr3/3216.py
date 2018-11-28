// https://code.google.com/codejam/contest/6224486/dashboard#s=p2
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <cstdint>

using namespace std;

enum {
	p1,
	pi,
	pj,
	pk,
	_1,
	_i,
	_j,
	_k
};

#if 0 
	1	i	j	k
1	1	i	j	k
i	i	-1	k	-j
j	j	-k	-1	i
k	k	j	-i	-1
#endif

const char table[8][8] = {
	{ p1, pi, pj, pk, _1, _i, _j, _k },	//1
	{ pi, _1, pk, _j, _i, p1, _k, pj },	//i
	{ pj, _k, _1, pi, _j, pk, p1, _i },	//j
	{ pk, pj, _i, _1, _k, _j, pi, p1 },	//k
	{ _1, _i, _j, _k, p1, pi, pj, pk },	//-1
	{ _i, p1, _k, pj, pi, _1, pk, _j },	//-i
	{ _j, pk, p1, _i, pj, _k, _1, pi },	//-j
	{ _k, _j, pi, p1, pk, pj, _i, _1 },	//-k
};

class solver
{
	vector<char> c;
	int64_t X;
	int L;
	int64_t N;
public:
	solver(const string& S, int64_t x) : L((int)S.size()), X(x), N(X*L)
	{
		c.resize(L);
		for (int i = 0; i < L; i++) {
			switch (S[i]) {
			case 'i': c[i] = pi; break;
			case 'j': c[i] = pj; break;
			case 'k': c[i] = pk; break;
			}
		}
	}

	inline int64_t f(int64_t i, int64_t n, char cur, char find)
	{
		for (; i < n; i++) {
			int j = i%L;
			cur = table[cur][c[j]];
			if (cur == find)
				return i;
		}
		return -1;
	}

	bool solve()
	{
		//漢の3重ループ！！！
		int cur_i = p1;
		for (int64_t i = 0; i < N - 2; i++) {
			i = f(i, N-2, cur_i, pi);
			if (i < 0) {
				return false;
			}
			int cur_j = p1;
			for (int64_t j = i + 1; j < N - 1; j++) {
				j = f(j, N - 1, cur_j, pj);
				if (j < 0) {
					return false;
				}
				int cur_k = p1;
				for (int64_t k = j + 1; k < N; k++) {
					k = f(k, N, cur_k, pk);
					if (k < 0) {
						return false;
					}
					if (k + 1 == N)
						return true;
					cur_k = pk;
				}
				cur_j = pj;
			}
			cur_i = pi;
		}
		return false;
	}
};

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int L;
		int64_t X;
		cin >> L >> X;
		string S;
		cin >> S;
		solver solver(S, X);
		bool ans = solver.solve();
		cout << "Case #" << (t + 1) << ": " << (ans?"YES":"NO") << endl;
	}
	return 0;
}
