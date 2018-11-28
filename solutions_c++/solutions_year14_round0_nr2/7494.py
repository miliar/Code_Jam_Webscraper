#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

double F,X,C;

int l,r;
double base;
double total;

void init(){
	l = r = 0;
	base = 2;
	total = 0;
}

void prework (){
	while ( F * X - C * base - F * C > 0){
		l ++;
		base += F;
	}
	r = l + 1;
}

double check (int res){
	double ret = 0;
	double tmp = 2;
	for (int i = 0;i < res;i ++){
		ret += C/tmp;
		tmp += F;
	}
	ret += X/tmp;
	return ret;
}

int main (){
	int cas,T = 0;
	freopen ("b.txt","r",stdin);
	freopen ("b.out","w",stdout);
	cin >> cas;
	while (cas --){
		scanf ("%lf%lf%lf",&C,&F,&X);
		int l = X / C - 1 - 2 / F;
		l = max (l,0);
//		printf ("%.7f\n",min (check (l) ,check (l + 1)));
//		printf ("%.7lf %.7lf\n",check (l),check (l + 1));
//		for (int i = 0;i < 100000;i ++){
//			double ret = check (i);
//			if (ret < 64.5) printf ("%d %.7lf\n",i,ret);
//		}
//		init();
//		prework();
//		printf ("l = %d r = %d\n",l,r);
//		double ans = check (l);
//		for (int i = 0;i <= 90;i ++){
//			printf ("%d %.7lf\n",i,check (i));
//		}
//	
//		ans = min (check (r),ans);
//Case #1: 
//		printf ("Case #%d: %.8lf\n",++ T,min (check (l),check (l + 1)));
	printf("Case #%d: %.8lf\n",++ T,min (check (l),check (l + 1)));	
	}
	return 0;
}
