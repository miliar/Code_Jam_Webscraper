#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef unsigned long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const LL inf = 1e+9;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;

#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);

#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "basket"

LD dp[201][201][201];

vector <vector <int> > g;

int bits(int x)
{
	int res = 0;
	while (x)
	{
		x &= (x - 1);
		res++;
	}
	return res;
}

int gmask;
int used = 0;
int N;
vector <int> p;
vector <vector <int> > ng;
bool go(int v)
{
	if (v == N)
		return true;
	bool fl = 0;
	for (int i = 0; i < N; i++)
	{
		if (((used & (1 << i)) == 0) && ng[p[v]][i])
		{
			used |= (1 << i);
			bool r = go(v + 1);
			if (r == false)
				return false;
			fl = 1;
			used ^= (1 << i);
		}
	}
	if (fl == 0)
		return false;
}
void solve()
{
	int T;
	scanf("%d", &T);

	for (int q = 0; q < T; q++)
	{
		cerr << q << endl;
		/*int N, K;
		scanf("%d %d", &N, &K);

		vector <LD> v(N);
		for (int i = 0; i < N; i++)
		{
			float f;
			scanf("%f", &f);
			v[i] = f;
		}

		dp[0][0][0] = 1;
		for (int i = 0; i < N; i++)
		{
			for (int k = 0; k <= max(i, K); k++)
				for (int v1 = 0; v1 <= K / 2; v1++)
					for (int last = 0; last <= i; last++)
					{
					dp[i + 1][k + 1][v1 + 1] +=  dp[last][k][v1] * v[i];
					dp[i + 1][k + 1][v1] +=  dp[last][k][v1] * (1 - v[i]);
					//dp[i + 1][k][v1] = max(dp[i + 1][k][v1], dp[i][k][v1]);
				}
		}

		cout.setf(ios::fixed);
		cout.precision(10);
		cout << "Case #" << q + 1 << ": " << dp[N][K][K / 2] << endl;

		for (int i = 0; i <= N; i++)
		{
			for (int k = 0; k <= K; k++)
				for (int v1 = 0; v1 <= K / 2; v1++)
				{
					dp[i][k][v1] = 0;
				}
		}*/

		scanf("%d", &N);
		g.clear();
		g.resize(N, vector <int>(N));
		int cmask = 0;
		int sz = 0;
		for (int i = 0; i < N; i++)
			for (int k = 0; k < N; k++)
			{
				int x;
				scanf("%1d", &x);
				g[i][k] = x;
				if (g[i][k])
					cmask |= (1 << sz);
				sz++;
			}

		int ans = 20;
		for (int mask = 0; mask < (1 << (N * N)); mask++)
		{
			if ((mask & cmask) != cmask)
				continue;

			int tmpAns = bits(mask - cmask);

			ng.clear();
			ng.resize(N, vector <int>(N));
			int sz2 = 0;
			for (int i = 0; i < N; i++)
				for (int k = 0; k < N; k++)
				{
					ng[i][k] = ((mask & (1 << sz2)) > 0);
					sz2++;
				}
			p.clear();
			p.resize(N);
			for (int i = 0; i < N; i++)
				p[i] = i;
			bool r = 1;
			do
			{
				used = 0;
				if (go(0) == false)
				{
					r = 0;
					break;
				}
			} while (next_permutation(all(p)));

			if (r)
				ans = min(ans, tmpAns);
		}

		cout << "Case #" << q + 1 << ": " << ans << endl;
	}

}

int main()
{
	
	//START
	//freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	solve();
	//END
	return 0;
}
/*******************************************
*******************************************/

template<typename T> istream & operator >> (istream &is, vector<T> &v)
{
	forn(i, v.size())
		is >> v[i];
	return is;
}
template<typename T> ostream & operator << (ostream &os, const vector<T> &v)
{
	forn(i, v.size())
		os << v[i];
	return os;
}
#endif