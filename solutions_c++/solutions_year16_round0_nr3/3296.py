#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <sstream>
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef pair <int, int> PII;
typedef vector <PII> VPII;
typedef vector <string> VS;

const double eps = 1e-9;
const int INF = 1000000007;
const int MOD = 1000000007;
const int MAXN = 10055;

VI p;
VB bp (MAXN, true);

void sievePrime()
{
	for (int i = 2; i < MAXN; ++ i)
	{
		if (bp[i])	p.PB(i);
		for (int j = 0; j < p.size() && p[j] * i < MAXN; ++ j)
		{
			bp[p[j] * i] = false;
			if (i % p[j] == 0)	break;
		}
	}
}

bool valid (int N, unsigned int x)
{
	VI fac (11, 0);
	for (int b = 2; b <= 10; ++ b)
	{
		for (int i = 0; i < p.size(); ++ i)
		{
			int sum = 0, pw = 1;
			for (int j = 0; j < N; ++ j)
			{
				if ((x >> j) & 1)
				{
					sum += pw;
				}
				pw = pw * b % p[i];
			}
			if (sum % p[i] == 0)
			{
				fac[b] = p[i];
				break;
			}
		}
		if (fac[b] == 0)	return	false;
	}
	
	for (int i = N - 1; i >= 0; -- i)
	{
		printf (((x >> i) & 1) ? "1" : "0");
	}
	for (int i = 2; i <= 10; ++ i)
	{
		printf (" %d", fac[i]);
	}
	puts ("");
}

int main()
{
	freopen ("C.in", "r", stdin);
	freopen ("C.out", "w", stdout);
	sievePrime ();
	
	int	T;	cin >> T;
	for (int cas = 1; cas <= T; ++ cas)
	{
		printf ("Case #%d:\n", cas);
		
		int N, L;
		cin >> N >> L;
		
		unsigned int x = (1 << N - 1);
		for (int i = 1; i < x && L; i += 2)
		{
//			cout << "x | i" << (x | i) << endl;
			if (valid (N, x | i))
			{
				-- L;
			}
		}
	}
	
	return 0;	
}
