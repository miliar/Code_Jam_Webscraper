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

int n, q;
int par[200];
vector<int> child[200];
char a[200];
string qs[10];
int childs[200];

#define K 30000
string res[K+5];

void back(int now)
{
	for(auto e : child[now])
	{
		back(e);
		childs[now]+=childs[e];
	}
	childs[now]++;
}

int main()
{
	int i, j, k, l;
	int T, TT;
	srand(time(NULL));
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		scanf("%d", &n);
		for(i=0;i<n;i++)
		{
			scanf("%d", &par[i]), par[i]--;
			if(par[i] != -1) child[par[i]].push_back(i);
		}
		scanf("%s", a);
		scanf("%d", &q);
		for(i=0;i<q;i++) cin>>qs[i];
		for(i=0;i<n;i++)
		{
			if(par[i] == -1) back(i);
		}
		for(i=0;i<K;i++)
		{
			vector<int> v;
			for(j=0;j<n;j++)
			{
				if(par[j] != -1) continue;
				for(k=0;k<childs[j];k++) v.push_back(j);
			}
			string now;
			for(j=0;j<n;j++)
			{
				int X=(rand()<<15)+rand();
				int x=X%v.size();
				int mi=MAX, ma=-1;
				for(k=0;k<v.size();k++)
				{
					if(v[k] == v[x])
					{
						mi=min(mi, k);
						ma=max(ma, k);
					}
				}
				int tar=v[x];
				v.erase(v.begin()+mi, v.begin()+ma+1);
				now.push_back(a[tar]);
				for(auto e : child[tar])
				{
					for(k=0;k<childs[e];k++) v.push_back(e);
				}
			}
			res[i]=now;
		}
		printf("Case #%d: ", T);
		for(i=0;i<q;i++)
		{
			int cnt=0;
			for(j=0;j<K;j++)
			{
				int good=0;
				for(k=0;k<n-qs[i].size()+1;k++)
				{
					int flag=0;
					for(l=0;l<qs[i].size();l++)
					{
						if(res[j][k+l] != qs[i][l])
						{
							flag=1;
							break;
						}
					}
					if(flag == 0)
					{
						good=1;
						break;
					}
				}
				if(good) cnt++;
			}
			printf("%.2lf ", (double)cnt/K);
		}
		for(i=0;i<n;i++) child[i].clear(), childs[i]=0;
		printf("\n");
	}
	return 0;
}
//*/