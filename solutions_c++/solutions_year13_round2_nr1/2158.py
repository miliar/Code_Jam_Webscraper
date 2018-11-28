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
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;


#define MAXSIZE 1000000

int dp[101][MAXSIZE+1];
int mote[100];

int main(){
	int T;
	cin>>T;
	rep(i,T){
		int a,n;
		cin>>a>>n;
		rep(i,n)cin>>mote[i];
		sort(mote,mote+n);
		rep(i,n+1)rep(j,MAXSIZE+1)dp[i][j]=INF;

		dp[0][a]=0;
		rep(i,n){
			rep(j,MAXSIZE+1){
				if(dp[i][j]==INF)continue;
				dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1);
				if(mote[i]<j){
					int t=min(MAXSIZE,j+mote[i]);
					dp[i+1][t]=min(dp[i+1][t],dp[i][j]);
				}else if(1<j){
					int lev=0,size=j;
					while(size<=mote[i]){
						lev++;
						size+=size-1;
					}
					int t=min(MAXSIZE,size+mote[i]);
					dp[i+1][t]=min(dp[i+1][t],dp[i][j]+lev);
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<*min_element(dp[n],dp[n]+MAXSIZE+1)<<endl;
	}
	return 0;
}