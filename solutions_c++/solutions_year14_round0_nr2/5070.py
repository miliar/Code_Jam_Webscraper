#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
#include<string.h>
using namespace std;
#define ll long int
//double a[max],b[max],dp[max];
int main(){
	int t;
	freopen("B-large.txt","w",stdout);
	 freopen("B-large.in","r",stdin);
		scanf("%d",&t);
	for(int k=1;k<=t;k++){
		double c,f,x,a,b,dp;
		scanf("%lf%lf%lf",&c,&f,&x);
		double t=2.00;
		a=c/t;
		b=x/t;
		double mini=b;
		t+=f;
		//int i=1;
		dp=0;
		while(dp+b>dp+a+x/t){
			dp+=a;
			a=c/t;
			b=x/t;
			t+=f;
		}
		printf("Case #%d: %.7lf\n",k,dp+b);
	}
	return 0;
}



