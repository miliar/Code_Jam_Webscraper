#include<stdio.h>

#define if if (
#define then )
#define do )
#define for for (
#define while while (
#define begin {
#define end }

int T;
double C,F,X;

inline double solve()
begin
	double ret=1e15;
	int i;
	double now=0;
	double rate=2.0;
	double tmp;
	for i=1;i<=100005;i++ do begin
		tmp=now+X/rate;
		if tmp<ret then ret=tmp;
		now+=C/rate;
		rate+=F;
	end;
	return ret;
end;

int main()
begin
	scanf("%d",&T);
	int tno=0;
	while T-- do begin
		++tno;
		scanf("%lf%lf%lf",&C,&F,&X);
		printf("Case #%d: ",tno);
		printf("%.7lf\n",solve());
	end;
end