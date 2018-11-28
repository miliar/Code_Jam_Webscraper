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
#include <assert.h>
#include <functional> //std::greater<int>
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll,ll> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(ll i = 0; i<(int)N; i++)
#define fornj(N)         for(ll j = 0; j<(int)N; j++)
#define fornk(N)         for(ll k = 0; k<(int)N; k++)
#define foreach(c,itr) for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
//#define MOD 1000007
#define awesome vector<int> A(N); forn(N) scanf("%d", &A[i]);
#define v vector
#define File "Patterns"
using namespace std;

int search(int ith, v<v<int> >& B)
{
	int N = B.size();
	v<int> A(N);
	forn(N) A[i] = B[i][ith];

	int ans = INF;
	forn(N)
	{
		int tmp = 0;
		fornj(N)
		{
			tmp += abs(A[i]-A[j]);
		}
		ans = min(ans, tmp);
	}
	return ans;
}
int main()
{
	#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
	#endif

	int T; cin >> T;
	for(int t = 1; t<=T; t++)
	{
		int A,B,K; cin >> A>>B>>K;
		ll ans = 0;
		for(int i = 0; i<A; i++)
		{
			for(int j = 0; j<B; j++)
			{
				if ((i&j) < K) ans++;
			}
		}
		printf ("Case #%d: %d\n", t, ans);
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}