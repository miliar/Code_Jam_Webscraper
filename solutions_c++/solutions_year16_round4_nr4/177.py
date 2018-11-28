//*
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

int n;
int a[5][5];
int b[5][5];

int puse[5];
int muse[5];

int rbad;

void check(int now)
{
	if(now == n) return;
	int i, j, k;
	for(i=0;i<n;i++)
	{
		if(puse[i]) continue;
		int flag=0;
		puse[i]=1;
		for(j=0;j<n;j++)
		{
			if(b[i][j] && !muse[j])
			{
				flag=1;
				muse[j]=1;
				check(now+1);
				muse[j]=0;
			}
		}
		puse[i]=0;
		if(!flag) rbad=1;
	}
}

int main()
{
	int i, j, k, l;
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		printf("Case #%d: ", T);
		cin>>n;
		for(i=0;i<n;i++)
		{
			char in[10];
			cin>>in;
			for(j=0;j<n;j++) a[i][j]=in[j]-'0';
		}
		int mi=MAX;
		for(j=0;j<(1<<(n*n));j++)
		{
			for(k=0;k<n*n;k++) b[k/n][k%n]=!!(j&(1<<k));
			int cnt=0, bad=0;
			for(k=0;k<n;k++) for(l=0;l<n;l++)
			{
				if(a[k][l] == 1 && b[k][l] == 0)
				{
					bad=1;
				}
				else if(a[k][l] == 0 && b[k][l] == 1) cnt++;
			}
			if(bad) continue;
			rbad=0;
			for(k=0;k<n;k++) puse[k]=muse[k]=0;
			check(0);
			if(!rbad) mi=min(mi, cnt);
		}
		printf("%d\n", mi);
	}
	return 0;
}
//*/