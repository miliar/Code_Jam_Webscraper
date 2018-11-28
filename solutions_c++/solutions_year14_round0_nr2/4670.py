#include<string>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<set>
using namespace std;
#define EPS 0.0000001
double calu(double c,double f,double x,int count){
	double a=0;
	for(int i=0;i<count;i++){
		a+=c/(2.0+i*f);
	}
	a+=x/(count*f+2.0);
	return a;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cases;
	cin>>cases;
	for(int t=1;t<=cases;t++){
		double c,f,x,abli;
		scanf("%lf %lf %lf",&c,&f,&x);
		double at=x/2;
		double ct=c/2+x/(2.0+f);
		int count=1;
		while(at-ct>=EPS){
			count++;
			at=ct;
			ct=calu(c,f,x,count);
		}
		printf("Case #%d: %.7lf\n",t,at);
	}
}