#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
using namespace std;

double mintime(double x,double c,double f1,double m){
	double p;
	if((x/m)>(c/m)+(x/(m+f1))){
		p=(c/m)+(mintime(x,c,f1,m+f1));
		return p;
	}
	else return (x/m);
}
int main()
{
	int t;
	scanf("%d",&t);
	double C,M,X;
	for(int i=0;i<t;i++){
		cin >> C >> M >>X;
		double T=mintime(X,C,M,2.0);
		printf("Case #%d: %.7lf \n",i+1,T);
	}
	return 0;
}