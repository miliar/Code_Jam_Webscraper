// Author : Ankit Bisla
 
#include<bits/stdc++.h>
 
using namespace std;
 
#define 	SZ(A) 		((int)A.size())
#define 	LEN(A) 		((int)A.length())
#define 	MS(A) 		memset(A, 0, sizeof(A))
#define 	MSV(A,a) 	memset(A, a, sizeof(A))
#define 	mp(x,y)		make_pair((x),(y))
#define 	pb(x) 		push_back(x)
#define		F 		first
#define 	S 		second
#define 	INF 		(ll(1e9))
#define 	INFL 		(ll(1e18))
#define 	EPS 		1e-12
 
#define 	chkbit(s, b) 	(s & (1<<b))
#define 	setbit(s, b) 	(s |= (1<<b))
#define 	clrbit(s, b) 	(s &= ~(1<<b))
 
#define 	swap(x,y)  	{x=x+y-(y=x);}
#define 	FOUND(A, x) 	(A.find(x) != A.end())
 
#define 	s(x) 		scanf("%d",&x);
#define 	s2(x,y) 	scanf("%d%d",&x,&y);
#define 	p(x) 		printf("%d\n",x);
#define 	p1d(a,n)        for(int i = 0; i < n; i++) printf("%d ",a[i]); printf("\n");
 
 
#define 	REP(i, n) 	for(i = 0; i < (n); i++)
#define 	FOR(i, a, n) 	for(i = a; i < n; i++)
#define 	REV(i, a, n) 	for(i = a; i >= n; i--)
#define 	FORALL(itr, c) 	for(itr = (c).begin(); itr != (c).end(); itr++)
#define 	ALL(A) 		A.begin(), A.end()
#define 	LLA(A) 		A.rbegin(), A.rend()
#define 	print(a,n)	REP(int i = 0; i < (n) ; i++)	pl(a[i]);
 
#define 	MOD	        1000000007
 
#define gc getchar//_unlocked
 
#define 	DEBUG 		1
#define 	TRACE 		1
 
#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif
 
typedef long long ll;
typedef unsigned long long llu;
 
typedef vector<int> VI;
typedef pair<int, int> II;
typedef vector<long long> VLL;
typedef vector<bool> VB;

#define N	1100000
int f = 0;
ll dp[N];

ll rev(ll num){
	ll ret = 0;
	while(num){
		ret = ret*10 + (num%10);
		num = num/10;
	}
	return ret;
}

ll rec(ll cur){
	if(cur == 1)	return dp[cur] = 1;
	ll rever = rev(cur);
	
	if(dp[cur]!=-1)	return dp[cur];
	
	ll ans1 = 1 + rec(cur - 1);
	ll ans2 = INF;
	if(rever < cur && cur%10!=0)
		ans2 = 1 + rec(rever);
	return dp[cur] = min(ans1,ans2);
}

void preprocess(){
	int i;
	REP(i,N)	dp[i] = -1;
	FOR(i,1,N)	rec(i);	
}
 
int main(){
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int t;
	ll n;
	cin>>t;
	
	preprocess();
	
	for(int qq=1;qq<=t;qq++){
		cin>>n;
		printf("Case #%d: %lld\n",qq,dp[n]);
	}
	return 0;
} 
