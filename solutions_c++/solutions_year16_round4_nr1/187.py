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

string ans;

string dodo(int now, char c)
{
	if(now == 0)
	{
		string res;
		res.push_back(c);
		return res;
	}
	string p1, p2;
	if(c == 'R') p1=dodo(now-1, 'R'), p2=dodo(now-1, 'S');
	else if(c == 'P') p1=dodo(now-1, 'P'), p2=dodo(now-1, 'R');
	else if(c == 'S') p1=dodo(now-1, 'P'), p2=dodo(now-1, 'S');
	if(p1 > p2) swap(p1, p2);
	return p1+p2;
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
		int n;
		int x, y, z;
		printf("Case #%d: ", T);
		cin>>n>>x>>y>>z;
		int flag=0;
		for(i=0;i<3;i++)
		{
			int now[3]={0, 0, 0};
			now[i]=1;
			for(j=0;j<n;j++)
			{
				int nex[3]={0,};
				nex[0]+=now[0], nex[2]+=now[0];
				nex[0]+=now[1], nex[1]+=now[1];
				nex[1]+=now[2], nex[2]+=now[2];
				for(k=0;k<3;k++) now[k]=nex[k];
			}
			if(x == now[0] && y == now[1] && z == now[2])
			{
				if(i == 0) ans=dodo(n, 'R');
				else if(i == 1) ans=dodo(n, 'P');
				else ans=dodo(n, 'S');
				printf("%s\n", ans.c_str());
				flag=1;
				break;
			}
		}
		if(!flag) printf("IMPOSSIBLE\n");
	}
	return 0;
}
//*/