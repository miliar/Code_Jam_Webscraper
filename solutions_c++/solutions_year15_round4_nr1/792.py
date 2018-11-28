#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define INF 2000000000
#define sz(x) ((int)(x).size())
#define fi first
#define sec second
#define SORT(x) sort((x).begin(),(x).end())
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define repn(i,a,n) for(int (i)=(a);(i)<(int)(n);(i)++)
#define EQ(a,b) (abs((a)-(b))<eps)
char f[200][200];
int R,C;
bool check(int x,int y)
{
	if(f[x][y]=='.')return true;
	else if(f[x][y]=='^')
	{
		for(int i=x-1;i>=0;i--)
		{
			if(f[i][y]!='.')return true;
		}
		return false;
	}
	else if(f[x][y]=='v')
	{
		for(int i=x+1;i<R;i++)
		{
			if(f[i][y]!='.')return true;
		}
		return false;
	}
	else if(f[x][y]=='<')
	{
		for(int i=y-1;i>=0;i--)
		{
			if(f[x][i]!='.')return true;
		}
		return false;
	}
	else
	{
		for(int i=y+1;i<C;i++)
		{
			if(f[x][i]!='.')return true;
		}
		return false;
	}
}
int tate[105],yoko[105];
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		memset(tate,0,sizeof(tate));
		memset(yoko,0,sizeof(yoko));
		scanf("%d %d",&R,&C);
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				cin >> f[i][j];
				if(f[i][j]!='.')
				{
					tate[i]++;
					yoko[j]++;
				}
			}
		}
		bool flag = false;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(f[i][j]!='.'&&tate[i]==1&&yoko[j]==1)
				{
					printf("Case #%d: IMPOSSIBLE\n",t+1);
					flag = true;
					goto end;
				}
			}
		}
		end:;
		if(flag)continue;
		int ans = 0;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(!check(i,j))ans++;
			}
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
