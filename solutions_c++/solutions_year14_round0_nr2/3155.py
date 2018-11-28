#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;

int C;
double cost,extra,goal;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&C);
	for(int tc=1;tc<=C;tc++){
		printf("Case #%d: ",tc);
		scanf("%lf%lf%lf",&cost,&extra,&goal);
		double ans=1e200;
		double sum=0;
		double rate=2;
		while(1){
			double tmp=sum+goal/rate;
			if(ans>tmp)
				ans=tmp;
			else
				break;
			sum+=cost/rate;
			rate+=extra;
		}
		printf("%.7f\n",ans);
	}
	return 0;
}