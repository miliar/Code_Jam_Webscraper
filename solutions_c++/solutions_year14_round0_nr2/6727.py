/*
 * problem2.cpp
 *
 *  Created on: 12-Apr-2014
 *      Author: cfilt
 */
#include <stdio.h>
int main(){
	int cases;
	scanf("%d",&cases);
	for(int c=1;c<=cases;++c){
		double C,F,X;
		double cur_rate=2.0;
		double totalTime=0.0;
		bool lotofCookies= false;
		scanf("%lf %lf %lf",&C,&F,&X);
		while(!lotofCookies){
			if((X/cur_rate)<=((C/cur_rate)+(X/(cur_rate+F)))){
				totalTime+=(X/cur_rate);
				lotofCookies =true;
				printf("Case #%d: %.7lf\n",c,totalTime);
			}else{
				totalTime+=(C/cur_rate);
				cur_rate+=F;
			}
		}
	}
	return 0;
}


