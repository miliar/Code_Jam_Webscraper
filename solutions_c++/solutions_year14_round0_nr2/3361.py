#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

double c,f,x;
double rate=2.0;

int isbuy(){
	double wintime=x/rate;
	double wintime2=c/rate+x/(rate+f);
	if(wintime-wintime2>1e-7){//需要买
		return 1;
	}else if(wintime-wintime2==1e-7){//不需要买了，直接等待结果
		return 0;
	}else{//不需要买
		return -1;
	}
}

int main(){
	freopen("E:\\C\\B-small-attempt0.in","r",stdin);
	freopen("E:\\C\\ans2.txt","w",stdout);
	int t,cc;
	int buynot;
	double mytime;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++){
		mytime=0.0;
		rate=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		buynot=isbuy();
		while(1){
			if(buynot==1){
				mytime+=c/rate;
				rate+=f;
				buynot=isbuy();
			}else{
				mytime += x/rate;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",cc,mytime);
	}

	return 0;
}