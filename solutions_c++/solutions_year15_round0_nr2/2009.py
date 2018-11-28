#include <bits/stdc++.h>
#define Int long long int
using namespace std;
int dp[1005][1005];
int main()
{
	int n,arr[1005];
	int i,j,k;
	for(i=1;i<=1002;i++){
		for(j=1;j<=1002;j++){
			if(j>=i){
				dp[i][j] = 0;
			}
			else{
				dp[i][j] = 100000000;
				for(k=1;k<i;k++)
					dp[i][j] = min(dp[i][j],1+dp[k][j]+dp[i-k][j]);
			}
		}
	}
	freopen("abc.in","r",stdin);
	freopen("out.txt", "w", stdout);
	int test,l=0;
	cin>>test;
	while(test--){
		l++;
		scanf("%d",&n);
		int ans = 0;
		for(i=0;i<n;i++){
			scanf("%d",&arr[i]);
			ans+=arr[i];
		}
		for(j=1;j<=1002;j++){
			int temp = 0;
			for(i=0;i<n;i++){
				temp+=dp[arr[i]][j];
			}
			temp+=j;
			ans = min(ans,temp);
		}
		cout<<"Case #"<<l<<": "<<ans<<"\n";
	}
    return 0;
}

/*

*/
