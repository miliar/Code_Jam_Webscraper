/*
ID: dixtosa1
PROG: milk2
LANG: C++11
*/
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
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
#include <bitset>
#include <functional> //std::greater<int>
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll, ll> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(long long i = 0; i < (long long)N; i++)
#define fornj(N)         for(long long j = 0; j < (long long)N; j++)
#define fornk(N)         for(long long k = 0; k < (long long)N; k++)
#define foreach(c,itr)   for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define awesome vector<int> A(N); forn(N) scanf("%d", &A[i]);
#define v vector
#define File "Patterns"
using namespace std;

int isPrime(ll num)
{
	if (num == 2) return 0;

	for (int i = 2; i*i <= num; i++)
	{
		if (num % i == 0) return i;
	}
	return 0;
}

ll mypow(int base, ll x)
{
	if (x == 1) return base;
	if (x % 2 == 1)
		return base * mypow(base, x - 1);
	else
		return mypow(base * base, x / 2);
}
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int T; cin >> T;
	for (int test = 1; test <= T; test++)
	{
		int N, J; cin >> N >> J;
		cout << "Case #" << test << ":" << endl;

		for (int bitmask = 0; bitmask < (1 << (N - 2)); bitmask++)
		{
			v<ll> divs;
			for (int base = 2; base <= 10; base++)
			{
				ll num = 1 + mypow(base, N - 1);
				for (int i = 1; i < N - 1; i++)
				{
					if ((bitmask & (1 << (i - 1))) > 0)
						num += mypow(base, i);
				}

				ll div = isPrime(num);
				if (div > 0) divs.push_back(div);
				else break;
			}
			if (divs.size() == 9)
			{
				string strbitmask = bitset<14>(bitmask).to_string();
				cout << 1 << strbitmask << 1;
				forn(9) cout << " " << divs[i];
				cout << endl;
				cerr << strbitmask << endl;
				cout.flush();
				J--;
				if (J == 0) break;
			}
		}
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}