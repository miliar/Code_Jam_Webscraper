#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main(){
	freopen("C.in","r",stdin); 
	freopen("CodeJam.out","w",stdout);
	
	double C,F,X,prod,time;
	double i,j,k,pq;
	bool flag;
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>C>>F>>X;
		flag =true;
		prod = 2.0;
		time = 0.00;
		while(flag){
			pq = X/prod;
			
			i = C/prod;
			j = prod + F;
			k = X/j+i;
			
			if(k<pq){
				time += i;
				prod += F;
			}
			else flag=false;
		}
		time+=X/prod;
		printf("Case #%d: %.7lf\n",t,time);
	}
	return 0;
}

