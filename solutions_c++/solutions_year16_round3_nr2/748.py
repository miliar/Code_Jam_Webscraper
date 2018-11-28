#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
#include <bitset>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(ll i = 0; i<(int)N; i++)
#define fornj(N)         for(ll j = 0; j<(int)N; j++)
#define fornk(N)         for(ll k = 0; k<(int)N; k++)
#define forn1(N)          for(ll i = 1; i<=(int)N; i++)
#define fornj1(N)         for(ll j = 1; j<=(int)N; j++)
#define fornk1(N)         for(ll k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
#define File "fileName"

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

#define log2BitApproximate(S) ((int)(log((double)S) / log(2.0)))
#define log2Bit(S) (1 << (log2BitApproximate(S) + 1) > S ? log2BitApproximate(S) : log2BitApproximate(S) + 1)
#define highBit(S) (isPowerOfTwo(S) ? S : 1 << log2Bit(S))

#define modulo(S, N) ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

using namespace std;

const ll MOD = 1000000007;

int myAb(int a)
{
	return a < 0 ? -a : a;
}




int main()

{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(t)
	{

		ll b, m;
		cin >> b >> m;

		//v<v<int> > adj(b, v<int>(b, 0));

		bool isSol = true;

		v<ll> numOfPaths(b, 0);
		numOfPaths[b - 1] = 1;

		for (int u = b - 2; u >= 0; --u)
		{
			for (int vv = u + 1; vv < b; ++vv)
				numOfPaths[u] += numOfPaths[vv];
		}

		v<int> takeOrNot(b, 0);
		int pt = 1;
		ll cpM = m;
		while (cpM != 0 && pt < b)
		{
			if (cpM - numOfPaths[pt] >= 0) {
				cpM -= numOfPaths[pt];
				takeOrNot[pt] = 1;
			}
			pt++;
		}
		

		
		cout << "Case #" << i + 1 << ": ";
		if (numOfPaths[0] < m)
			cout << "IMPOSSIBLE" << endl;
		else {
			cout << "POSSIBLE" << endl;
			fornj(b)
				cout << takeOrNot[j];
			cout << endl;
			for (int j = 1; j < b; ++j)
			{
				for (int k = 0; k < b; ++k)
				{
					if (k > j) cout << 1;
					else cout << 0;
				}
				cout << endl;
			}
		}



		
	}

	return 0;
}