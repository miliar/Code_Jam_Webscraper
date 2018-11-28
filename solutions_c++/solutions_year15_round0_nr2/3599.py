#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll dp[1005][1005],a[1005];
void func()
{
	int i,j,k;
	for(int i=1;i<=1004;i++)
	for(int j=i+1;j<1005;j++)
	{
		dp[i][j] = 10000;
		for(k=i;k<=(i+j)/2;k++)
		dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j-k] + 1);
	}
}
int main()
{	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	func();
	int i,t,d,k;
	cin>>t;
	int j = t;
	while(t--){
		cin>>d;
		for(int i=0;i<d;i++)
		cin>>a[i];
		int ans = 1005;
		for(k=1;k<1005;k++){
			int temp = 0;
			for(int i=0;i<d;i++)
			temp += dp[k][a[i]];
			temp += k;
			ans = min(ans,temp);
		}
		cout<<"Case #"<<j-t<<": "<<ans<<endl;
	}
	return 0;
}
