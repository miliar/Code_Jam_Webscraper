#include<bits/stdc++.h>
using namespace std;
int dp[1003][1003];
void preprocess()
{
    int i,j,k;
    for(i = 1; i <= 1001; i++) {
        for(j = i+1; j <= 1001; j++) {
            dp[i][j] = 10000;
            for(k = i; k <= (i+j)/2; k++) {
                dp[i][j] = min(dp[i][j] , dp[i][k] + dp[i][j-k] + 1);
            }
        }
    }
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("QR2.txt","w",stdout);
    int i,j,n,t,k,res,x;
    cin>>t;
    preprocess();
    int tc = 1;
    while(t--) {
        cin>>n;
        int a[n];
        for(i = 0; i < n; i++) {
            cin>>a[i];
        }
        res = 1001;
        for(k = 1; k <= 1001; k++) {
            x = 0;
            for(i = 0; i < n; i++) {
                x += dp[k][a[i]];
            }
            x += k;
            res = min(res,x);
        }
        cout<<"Case #"<<tc<<": "<<res<<endl;
        tc++;
    }
    return 0;
}
