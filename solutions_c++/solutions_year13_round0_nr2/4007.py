#pragma comment(linker, "/STACK:16777216")
#include <iostream>
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
#include <functional>


//#include <sstream>
//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

#define ll long long
#define all(x)          (x).begin(), (x).end()
#define forn(N)         for(ll i = 0; i<N; i++)
#define fornj(N)         for(ll j = 0; j<N; j++)
#define PI 3.1415926535897932384626433
#define INF 2147483647
//#define MOD 1000007
using namespace std;


//#define ONLINE_JUDGE
//#undef ONLINE_JUDGE

int grid[101][101];

int N,M;

bool isValid(int i, int j)
{
	int ans = 0;
	for(int ii = 0; ii<N; ii++)
	{
		if (grid[ii][j]>grid[i][j])
		{
			ans++;break;
		}
	}
	for(int jj = 0; jj<M; jj++)
	{
		if (grid[i][jj]>grid[i][j])
		{
			ans++;break;
		}
	}
	if (ans == 2) return false;
	return true;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#endif

	int T;
	cin>>T;
	N=100;
	M=100;
	for(int t = 1; t<=T; t++)
	{
		cin>>N>>M;
		forn(N)
		{
			fornj(M)
			{
				cin>>grid[i][j];
			}
		}

		bool ans = true;

		forn(N)
		{
			fornj(M)
			{
				ans &= isValid(i,j);
			}
		}

		if (ans)
			cout<<"Case #"<<t<<": YES"<<endl;
		else
			cout<<"Case #"<<t<<": NO"<<endl;
	}
	
	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}