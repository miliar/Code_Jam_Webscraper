#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
typedef pair<int,int> PII;

const int NMAX=1000;
const int MMAX=100;
const int MOD=1000000007;

int N,M; string S[NMAX]; int LCP[NMAX];
int now[MMAX];
int a1,a2;

void dfs(int dep,int cst,int msk)
{
	if(dep==N)
	{
		if(msk+1==1<<M){if(cst>a1){a1=cst;a2=1;}else if(cst==a1)a2++;}
		return;
	}
	int was[MMAX];
	memcpy(was,now,M*sizeof(int));
	for(int i=0;i<M;i++)now[i]=min(now[i],LCP[dep]);
	for(int i=0;i<M;i++)
	{
		const int t=now[i];
		now[i]=S[dep].size();
		dfs(dep+1,cst+S[dep].size()-t,msk|1<<i);
		now[i]=t;
	}
	memcpy(now,was,M*sizeof(int));
}

PII solve()
{
	a1=-1;a2=0;
	dfs(0,M,0);
	return PII(a1,a2);
}

void build()
{
	sort(S,S+N);
	for(int i=1;i<N;i++)
	{
		int j=0;
		while(S[i-1][j]==S[i][j])j++;
		LCP[i]=j;
	}
}

void input()
{
	cin>>N>>M;
	for(int i=0;i<N;i++)cin>>S[i];
}

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		input();
		build();
		const PII ans=solve();
		cout<<"Case #"<<t<<": "<<ans.first<<' '<<ans.second<<endl;
	}
	return 0;
}
