#include<stdio.h>
#include<algorithm>
int tcn,tc;
int n,m;
double a[210];
double dpa[210][210];
double dpb[210][210];
double ans;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%lf",&a[i]);
		}
		std::sort(a,a+n);
		for(i=0;i<=n;i++){
			for(j=0;j<=m;j++){
				dpa[i][j]=0;
				dpb[i][j]=0;
			}
		}
		dpa[0][0]=1;
		dpb[0][0]=1;
		for(i=0;i<n;i++){
			for(j=0;j<=m;j++){
				dpa[i+1][j]+=dpa[i][j]*a[i];
				dpa[i+1][j+1]+=dpa[i][j]*(1-a[i]);
				dpb[i+1][j]+=dpb[i][j]*a[n-1-i];
				dpb[i+1][j+1]+=dpb[i][j]*(1-a[n-1-i]);
			}
		}
		ans=0;
		for(i=0;i<=m;i++){
			double tans=0;
			for(j=0;j<=m/2;j++){
				tans+=dpa[i][j]*dpb[m-i][m/2-j];
			}
			if(tans>ans)ans=tans;
		}
		printf("Case #%d: %.10lf\n",tc,ans);
	}
	return 0;
}