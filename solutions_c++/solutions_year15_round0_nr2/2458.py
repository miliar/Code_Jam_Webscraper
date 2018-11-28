#include<cstdio>
#include<algorithm>
#include<iostream>

using namespace std;

const int N = 1010;

int dp[N][N],arr[N];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) dp[i][j]=N*N;
    }
    for(int i=1;i<N;i++) {
        for(int j=1;j<N;j++) {
            if(i<=j) dp[i][j]=0;
            for(int k=1;k<i;k++) dp[i][j]=min(dp[i-k][j]+dp[k][j]+1,dp[i][j]);;
        }
    }
    int t,p,n,k;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++) {
        scanf("%d",&p);
        for(int i=0;i<p;i++) scanf("%d",&arr[i]);
        int ans=N*N;
        for(int i=1;i<N;i++) {
            int temp=i;
            for(int j=0;j<p;j++) temp+=dp[arr[j]][i];
            if(ans>temp) ans=temp;
        }
        printf("Case #%d: %d\n",cas,ans);
        //cout<<"Case #"<<cas<<" :"<<dp[n]<<endl;
    }
    return 0;
}
