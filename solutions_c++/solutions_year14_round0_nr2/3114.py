#include<stdio.h>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	double c,f,x;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lf%lf%lf",&c,&f,&x);
		double u = x/c - 1 - 2/f,ans = 0;
		int i;
		for(i=0;i<u;i++){
			ans+=c/(2+f*i);
		}
		ans+=x/(2+f*i);
		printf("Case #%d: %.7f\n",t,ans);
	}
	return 0;
}
