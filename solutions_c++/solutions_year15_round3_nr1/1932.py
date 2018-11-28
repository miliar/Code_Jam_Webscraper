#include <cstdio>
#include <iostream>
using namespace std;

int w,t;
int dp[21][21], r,c;
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int cas = 1;
	for(int i = 0; i < 21; ++i){
		for(int j = 1; j < 21; ++j){
			dp[i][j] = -1000;
		}
	}
	for(int i = 1; i < 21; ++i){
		for(int j = 1; j <= i; ++j){
			if(i == j){
				dp[i][j] = j;
			}else{
				int _min = 10000;
				for(int k = 0; k < i; ++k){
					int l = min(k,j-1);
					int r = min(i-1-k, j-1);
					int ans = max(dp[l+r][j-1],dp[k][j]+(i-k-1)/j);
					ans = max(ans, dp[i-1-k][j]+(k)/j);
					_min = min(ans,_min);
				}
				dp[i][j] = _min+1;
			}
		}
	}
/*	
	for(int i = 1; i < 21; ++i){
		for(int j = 1; j <= i; ++j){
			cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
		}
	}
*/	
	while(cas <= t){
		cout<<"Case #"<<cas++<<": ";
		cin>>r>>c>>w;
		cout<<dp[c][w]<<endl;
	}
}
