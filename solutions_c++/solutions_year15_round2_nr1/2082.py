/*
-----------------------------------------------------------------------------
Author :            ---------------------------------------------------------
    UTKAR$H $AXENA  ---------------------------------------------------------
    IIT INDORE      ---------------------------------------------------------
-----------------------------------------------------------------------------
*/
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define fre 	freopen("A-small-attempt0.in","r",stdin),freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define M 1000000007
#define lld signed long long int
#define pp pop_back()
#define ps(x) push_back(x)
#define mpa make_pair
#define pii pair<int,int>
#define fi first
#define se second
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define boost ios_base::sync_with_stdio(0)
//vector<int> g[2*100000+5];
int visited[2*1000000+5];
int ans[1000000+5];
pii give(int x)
{
	pii t;
	int r=0;
	int y=x+1;
	while(x>0)
	{
		r=10*r+(x%10);
		x/=10;
	}
	return mpa(y,r);
}
int main()
{
	fre;
	queue<pii >Q;
	Q.push(mpa(1,1));
	while(not Q.empty())
	{
		int T=Q.front().fi;
		int D=Q.front().se;
		Q.pop();

		if(T>1000000 or visited[T])
			continue;
		ans[T]=D;
		visited[T]=1;

		pii P=give(T);
		Q.push(mpa(P.fi,D+1));
		Q.push(mpa(P.se,D+1));
	}
	int t,N;
	cin>>t;
	for(int T=1;T<=t;++T)
	{
		cin>>N;
		printf("Case #%d: %d\n",T,ans[N]);
	}
}
