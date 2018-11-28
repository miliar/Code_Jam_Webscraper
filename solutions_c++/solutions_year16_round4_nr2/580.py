//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
int n,k;
double s[402];
double ss[402];
double dp[202][102][102]; // yes,no
int main(void){
    int t;
    scanf("%d",&t);
    int hh;
    for(hh=1;hh<=t;hh++){
		scanf("%d%d",&n,&k);
		int i,j,l,st;
		for(i=0;i<n;i++)
			scanf("%lf",&s[i]);
		sort(s,s+n);
		for(i=0;i<n;i++){
			s[i+n]=s[i];
		}
		double ans=0;
		for(st=0;st<n;st++){
			for(i=st;i<st+k;i++)
				ss[i-st]=s[i];
			for(i=0;i<202;i++)
				for(j=0;j<102;j++)
					for(l=0;l<102;l++)
						dp[i][j][l]=0;
			dp[0][0][0]=1, dp[0][1][0]=ss[0], dp[0][0][1]=1-ss[0];
			for(i=1;i<n;i++)
				for(j=0;j<=k/2;j++)
					for(l=0;l<=k/2;l++){
						dp[i][j][l]+= dp[i-1][j][l];
						if(j>0) dp[i][j][l]+=dp[i-1][j-1][l]*ss[i];
						if(l>0) dp[i][j][l]+=dp[i-1][j][l-1]*(1-ss[i]);
					}
					
			ans=max(ans,dp[k-1][k/2][k/2]);
		}
		printf("Case #%d: %.8lf\n",hh,ans);
	}
    return 0;
}
