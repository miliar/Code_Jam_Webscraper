#include<stdio.h>
#include<algorithm>

int chk[2050];
double *ord[2050];
double inp[2050];

bool comp(const double *a, const double *b){return *a<*b;}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,n;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d",&n);
		for(int i=1;i<=2*n;i++)scanf("%lf",inp+i);
		for(int i=1;i<=2*n;i++)ord[i]=inp+i;
		std::sort(ord+1,ord+2*n+1,comp);
		for(int i=1;i<=2*n;i++){
			if(ord[i]-inp<=n)chk[i]=1;
		}
		int ans[2]={n},now=0;
		for(int i=1;i<=2*n;i++){
			if(chk[i])now++;
			else if(now>0)now--,ans[0]--;
		}
		now=0;
		for(int i=1;i<=2*n;i++){
			if(!chk[i])now++;
			else if(now>0)now--,ans[1]++;
		}
		printf("Case #%d: %d %d\n",t,ans[1],ans[0]);
		for(int i=1;i<=2*n;i++)chk[i]=false;
	}
	return 0;
}
