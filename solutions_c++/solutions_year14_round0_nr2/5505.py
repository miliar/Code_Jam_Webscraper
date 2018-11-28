#include <stdio.h>

double C,F,X;

void input()
{
	scanf("%lf %lf %lf",&C,&F,&X);
}

void process()
{
	int cnt=(X/C)-(2.0/F);

	cnt-=2;
	if(cnt<0) cnt=0;

	double ti=0,cr=2; 
	for(int i=0; i<cnt; i++) {
		ti+=C/cr;
		cr+=F;
	}
	double sum=ti+(X/cr);
	for(int i=cnt;i<=cnt+5;i++) {
		ti+=C/cr;
		cr+=F;
		if(sum>ti+(X/cr)) sum=ti+(X/cr);
	}
	printf("%.7lf",sum);
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d: ",i);
		input();
		process();
		printf("\n");
	}
	return 0;
}