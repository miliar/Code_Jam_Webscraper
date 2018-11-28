//============================================================================
// Name        : code.cpp
// Author      : vlade087
// Version     : 1.0
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<sstream>
#include<math.h>
#include<ctype.h>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<algorithm>
#include <complex>
#include <numeric>
#include<list>
#include<deque>
#include <stdlib.h>
#define mod 1000000007
#define inf 200000000000000L
#define countbits __builtin_popcount
#define sz sizeof
#define mp make_pair
#define pb push_back
#define ll long long
#define ull unsigned long long
#define mset memset
#define sz sizeof
#define maxn 2000
#define EPS 1e-9
#define par pair<int,int>
using namespace std;
int n,m,k,y,tt;
double A[maxn],B[maxn];
bool use[maxn];
int f[8] = {-1,-1,-1,0,1,1,1,0};
int c[8] = {-1,0,1,1,1,0,-1,-1};
char C[60][60],T[60][60];
bool esta(int xx,int yy)
{
	return xx>=0&&xx<n&&yy>=0&&yy<m;
}
void printC()
{
	C[n-1][m-1] = 'c';
	for(int i=0; i < n;i++)
	{
		for(int j = 0; j < m;j++)
			printf("%c",C[i][j]);
		printf("\n");
	}
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&tt);
	for(int w = 1; w<=tt;w++)
	{
		scanf("%d",&n);
		for(int i = 0; i < n;i++)
			scanf("%lf",A+i);
		for(int i = 0; i < n;i++)
			scanf("%lf",B+i);
		sort(A,A+n);
		sort(B,B+n);
		mset(use,0,sz(use));
		int war = 0;
		for(int i = n-1;i>=0;i--)
		{
			int ok = 1;
			for(int j=0; j < n && ok;j++)
				if(!use[j] && B[j] > A[i])
				{
					ok = 0;
					use[j]=1;
				}
			war = war + ok;
		}
		mset(use,0,sz(use));
		int dwar = 0;
		int ini = 0 , fin = n-1;
		int fin1 = n-1;
		while(ini<=fin)
		{
			if(A[fin] > B[fin1])
			{
				fin--;
				fin1--;
				dwar++;
			}else {
				ini++;
				fin1--;
			}
		}
		printf("Case #%d: %d %d\n",w,dwar,war);
	}
	return 0;
}
