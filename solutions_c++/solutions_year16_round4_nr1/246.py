#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
vector<string>f[110];
map<string,string>ooxx;
string get(string str)
{
	int n=str.size();
	n/=2;
	string a="";
	for(int i=0;i<n;i++)
		a+=str[i];
	a=ooxx[a];
	string b="";
	for(int i=n;i<n+n;i++)
		b+=str[i];
	b=ooxx[b];
//	cout << a << " " << b << endl;
	if(a < b)
		return a+b;
	return b+a;
}
void init()
{
	f[1].pb("PR");
	ooxx["P"]="PR";
	f[1].pb("PS");
	ooxx["S"]="PS";
	f[1].pb("RS");
	ooxx["R"]="RS";
	for(int t=1;t<12;t++)
	{
		for(int i=0;i<3;i++)
		{
			string str=get(f[t][i]);
			ooxx[f[t][i]]=str;
			f[t+1].pb(str);
		}
	}
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
//	freopen("A.out","w",stdout);
	init();
//	return 0;
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,r,p,s;
		scanf("%d %d %d %d",&n,&r,&p,&s);
		string ans="z";
		for(int i=0;i<3;i++)
		{
			int R,P,S;
			R=P=S=0;
			int len=f[n][i].size();
			for(int j=0;j<len;j++)
			{
				if(f[n][i][j] == 'R')
					R++;
				if(f[n][i][j] == 'P')
					P++;
				if(f[n][i][j] == 'S')
					S++;
			}
			if(R == r && P == p && S == s)
				ans=min(ans,f[n][i]);
		}
		if(ans == "z")
			ans="IMPOSSIBLE";
		printf("Case #%d: ",cc);
		cout << ans << endl;
	}
	return 0;
}
/*
4
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2

1
2 2 1 1

 */
