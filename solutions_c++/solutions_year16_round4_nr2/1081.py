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
#define fre 	freopen("0.in","r",stdin);freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
#define LL signed long long int
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define rep(i,from,to) for(int i=(from);i <= (to); ++i)
#define pii pair<int,int>

vector<int> G[2*100000+5];
double dp[205][205];
int OFF = 205;
double P[654];
int N,K;
double tell(int mask){
	vector<double>V;
	rep(i,0,N-1){
		if(mask&(1<<i))V.push_back(P[i]);
	}
	dp[0][OFF ] = 1;
	for(int i=1;i<=K;++i){
		for(int o=-i;o<=i;++o){
			dp[i][o+OFF] = dp[i-1][o-1+OFF]*V[i-1] + dp[i-1][o+1+OFF]*(1-V[i-1]);
		}
	}
	double x = dp[K][OFF];
	for(int i=1;i<=K;++i){
		for(int o=-i;o<=i;++o){
			dp[i][o+OFF] = 0;//dp[i-1][o-1+OFF]*V[i-1] + dp[i-1][o+1+OFF]*(1-V[i-1]);
		}
	}
	return x;
}
int main(){
	fre;
	int T;
	cin>>T;

	rep(t,1,T){
		printf("Case #%d: ",t);
		cin>>N>>K;
		rep(i,0,N-1){
			cin>>P[i];
		}
		double ans = 0;
		for(int mask=0;mask<(1<<N);++mask){
			if(__builtin_popcount(mask)==K){
				ans = max(ans,tell(mask));
			}
		}
		printf("%0.12f\n",ans);
	}
}
