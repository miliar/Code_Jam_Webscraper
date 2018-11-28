#include<algorithm>
#include<stdio.h>
//#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<queue>
using namespace std;
int t;
int all;
double c,f,x;
double ma;
double s[10000005],sp;
int m;
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.txt","w",stdout);
	scanf("%d",&t);
	for(all=1;all<=t;all++){
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",all);
		ma=x/2;s[0]=0;
		for(m=1;;m++){
			s[m]=s[m-1]+c/((m-1)*f+2);
			if(s[m]>ma)break;
			sp=m*f+2;
			if(s[m]+x/sp<ma)ma=s[m]+x/sp;
			//printf("%lf ",s[m]);
		}
		printf("%.7lf\n",ma);
	}
	return 0;
}

