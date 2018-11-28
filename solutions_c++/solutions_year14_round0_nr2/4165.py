#include<cstdio>
#include<algorithm>
#include<conio.h>
#include<map>
#include<climits>
#include<vector>
#include<iostream>
using namespace std;

double minimum(double a,double b){
	if(a<b){
		return a;
	}
	return b;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	double C,F,X,result,pivot;
	result = 0;
	for(int i=1;i<=tc;i++){
		pivot = 2.0;
		result = 0;
		scanf("%lf%lf%lf",&C,&F,&X);
		while(true){
			double cost1 = (double)X/pivot;
			double cost2 = (double)C/pivot + (double)X/(pivot+F);
			if(cost1<cost2){
				result += X/pivot;
				break;
			}
			result += C/pivot;
			pivot += F; 
			//cout<<"cost1 "<<cost1<<" cost2 is "<<cost2<<" pivot is "<<pivot<<" result is "<<result<<endl;
		}
		//Case #1: 1.0000000
		printf("Case #%d: %.7lf\n",i,result);
	}
	return 0;
}

