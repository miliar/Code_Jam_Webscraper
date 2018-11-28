#include <cstdio>
double dp[213][213][213];
double a[213];
int T;
double prob[213];
double ans;
int n,k;
void p(int x, int y){
/*	printf("%d %d\n",x,y);
	for (int i=0;i<=n;i++){
		printf("%f ",prob[i]);
	}
	printf("\n");*/
	if (x==n){
		if (y==k){
			ans = ans>prob[k/2]?ans:prob[k/2];
		}
	}
	else{
		p(x+1,y);
		if (y<k){
			double prob2[213];
			for (int i=0;i<=k;i++){prob2[i] = prob[i];prob[i]=0;}
			for (int i=0;i<=k;i++){
				prob[i] = prob2[i]*(1.0-a[x]) + (i>0?prob2[i-1]*a[x]:0.0);
			}
			p(x+1,y+1);
			
			for (int i=0;i<=n;i++){prob[i] = prob2[i];}
		}
	}
}
int main(){
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		ans=0.0;
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++){
			scanf("%lf",&a[i]);
		}
		prob[0]=1.0;
		p(0,0);
		printf("Case #%d: %f\n",Case, ans);
		
	}
	return 0;
}
