//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
using namespace std;

int m,n,ans,tot;
string s[10];
vector<int> server[10];

void dfs(int i)
{
	if (i == m)
	{
		// pre-check
		FORN(j,n)
			if (server[j].sz() == 0)
				return;
		// check
		int tmp = 0;
		FORN(j,n)
		{
			set<string> st;
			FORN(k,server[j].sz())
				FORN(l,s[server[j][k]].sz())
				{
					string stmp;
					FORS(a,0,l)
						stmp += s[server[j][k]][a];
					st.ins(stmp);
				}
			tmp += (int)st.sz()+1;
		}
		if (tmp > ans)
		{
			ans = tmp;
			tot = 1;
		}
		else if (tmp == ans)
			tot++;
	}
	else
	{
		FORN(j,n)
		{
			server[j].pb(i);
			dfs(i+1);
			server[j].popb();
		}
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d%d",&m,&n);
		FORN(j,m)
			cin >> s[j];
		ans = 0,tot = 0;
		dfs(0);
		printf("Case #%d: %d %d\n",i+1,ans,tot);
	}
}
