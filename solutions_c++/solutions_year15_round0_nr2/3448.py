# include<bits/stdc++.h>
using namespace std;
#define N 1100
int dp[N][N];//dp[i][j]=no of special minutes to divide i pancakes in to plates all having less than or equal to j pancakes
void cal_dp(){
	for(int i=1;i<N;i++){
		for(int j=i;j<N;j++)
			dp[i][j]=0;
	}
	for(int i=2;i<N;i++){
		for(int j=1;j<i;j++){
            dp[i][j]=i-j+1;
			for(int k=1;k<=i/2;k++){//k is split size
				dp[i][j]=min(dp[i][j],1+dp[k][j]+dp[i-k][j]);
			}
		}
	}
}
int main(){
	cal_dp();
    int t,d,ans;
    int P[N];
    cin>>t;
    for(int i = 1; i <= t; i++)
    {   ans=0;
        cin>>d;
        for(int j = 1; j <= d; j++){
            cin>>P[j];
            if(ans<P[j])ans=P[j];
        }
        for(int j=1;j<ans;j++){//make each element less than j and then let them eat
            int sum=j;
            for(int x=1;x<=d;x++){
                sum+=dp[P[x]][j];
            }
            ans=min(sum,ans);
        }
        printf("Case #%d: %d\n",i,ans);
    }
}

