// Wsl_F

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

const int MaxN = 50;
LL pw[64];
int g[MaxN + 5][MaxN + 5];

void gen(int n)
{
	memset(g, 0, sizeof(g));
	for (int i = 1; i < n; i++)
		for (int j = i + 1; j <= n; j++)
			g[i][j] = 1;
}

void print(int b)
{
	cout << "POSSIBLE" << endl;
	for (int i = 1; i <= b; i++)
	{
		for (int j = 1; j <= b; j++)
			cout << g[i][j];
		cout << endl;
	}
}


void solve()
{
	LL b, M;
	cin >> b >> M;
	if (M == 1)
	{
		memset(g, 0, sizeof(g));
		g[1][b] = 1;
		print(b);
		return;
	}

	if (pw[b - 2] < M)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	int pwI = 0;
	while (pw[pwI] < M) pwI++;

	gen(pwI + 1);

	//LL cur = pw[pwI - 1];
	LL rest = M ;
	if (pw[pwI] == M)
	{
		g[1][b] = 1;
		rest--;
	}

	int i = 1;
	while (rest > 0)
	{
		if (rest % 2 == 1)
		{
			g[i + 1][b] = 1;
		}
		++i;
		rest /= 2;
	}

	print(b);
}

int main()
{
 ios_base::sync_with_stdio(0);
 cin.tie(0);
 srand(__rdtsc());

 //freopen("B-small-attempt1.in", "r", stdin);
 //freopen("B-small-output.txt", "w", stdout);

 freopen("B-large.in","r",stdin);
 freopen("B-large-output.txt","w",stdout);
 //cout<<fixed;
 //cout<<setprecision(9);

 pw[0] = 1;
 for (int i = 1; i < 64; i++)
	 pw[i] = pw[i - 1] * 2;

 int T;
 cin>>T;
 for (int testCase= 1; testCase <= T; testCase++)
 {
     cout<<"Case #"<<testCase<<": ";
     solve();
 }


 return 0;
}
