#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
double C,F,X;
double sum=2;
double ans=0;
double t1=0,t2=0;

double buy(){
	double K=C/sum;
	sum+=F;
	return K;
}

double wait(){
	return X/sum;
}

int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		t1=0,t2=0;sum=2.0;ans=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		ans=X/sum;
		while(1){
			t2=t1+wait();
			if(ans>=t2){
				ans=t2;
			}
			else break;
			t1+=buy();
		}
		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 0;
}
