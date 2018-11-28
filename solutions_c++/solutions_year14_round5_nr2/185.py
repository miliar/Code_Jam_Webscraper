#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <memory.h>

using namespace::std;

int P,Q,ans,N;
int life[105];
int point[105];
int dp[101][201][1005][4];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++){
		ans=0;
		scanf("%d %d %d",&Q,&P,&N);
		for(int i=0;i<N;i++)
			scanf("%d %d",&life[i],&point[i]);
		life[N]=0;
		for(int i=0;i<=N;i++)
			for(int j=life[i];j>=0;j--)
				for(int k=0;k<=1000;k++)
					for(int l=0;l<=1;l++)
						dp[i][j][k][l]=0;
		dp[0][life[0]][0][1]=1;
		for(int i=0;i<N;i++){
			for(int k=0;k<=1000;k++)
				for(int l=0;l<=1;l++){
					int now=dp[i][life[i]][k][l];
					if(now==0) continue;
					for(int k1=1;k1<=k;k1++){
						if(k1*Q<life[i]) dp[i][life[i]-k1*Q][k-k1][l]=max(dp[i][life[i]-k1*Q][k-k1][l],now);
						else if((k1-1)*Q<life[i]) dp[i+1][life[i+1]][k-k1][l]=max(dp[i+1][life[i+1]][k-k1][l],now+point[i]);
						else break;
					}
				}
			for(int j=life[i];j>=1;j--){
				for(int k=0;k<=1000;k++){
					for(int l=1;l>=0;l--){
						if(dp[i][j][k][l]!=0){
							int now=dp[i][j][k][l];
							int nl=(l+1)%2;
							if(l%2==0){
								if(j>P){
									dp[i][j-P][k][nl]=max(dp[i][j-P][k][nl],now);
								}
								else dp[i+1][life[i+1]][k][nl]=max(dp[i+1][life[i+1]][k][nl],now);
							}
							else if(l==1){
								dp[i][j][k][nl]=max(dp[i][j][k][nl],now);
								dp[i][j][k+1][nl]=max(dp[i][j][k+1][nl],now);
								if(j>Q){
									dp[i][j-Q][k][nl]=max(dp[i][j-Q][k][nl],now);
								}
								else{
									dp[i+1][life[i+1]][k][nl]=max(dp[i+1][life[i+1]][k][nl],now+point[i]);
								}
							}
							else{
								dp[i][j][k][nl]=max(dp[i][j][k][nl],now);
							}
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",ca,max(max(dp[N][0][0][1],dp[N][0][0][0]),max(dp[N][0][0][2],dp[N][0][0][3]))-1);
	}
	return 0;
}