#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

int dp[6];
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	int E,R,N;
	cin>>T;
	rep(i,T){
		cin>>E>>R>>N;
		memset(dp,0,sizeof(dp));
		rep(j,N){
			int v;
			cin>>v;
			rep(k,E+1){
				rep(l,k+1){
					dp[k-l] = max(dp[k-l],dp[k]+v*l);
				}
			}
			for(int k=E-R;k>=0;k--){
				dp[k+R]=max(dp[k+R],dp[k]);
			}
		}
		cout<<"Case #"<<i+1<<": "<<*max_element(dp,dp+6)<<endl;
	}
	return 0;
}