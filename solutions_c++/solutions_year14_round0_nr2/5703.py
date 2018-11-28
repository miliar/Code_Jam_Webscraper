#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		double C,F,X;
		cin>>C>>F>>X;
		double sum = 0;
		double time = 0;
		double speed = 2;
		while(sum < X){
			sum += C;
			time += C/speed;
			if((X - sum + C)/(speed + F) < (X - sum) / speed){
				sum -= C;
				speed += F;
			}
			if(sum + C >= X){
				time +=(X - sum) /speed;
				break;
			}
		}
		
		
		cout<<"Case #"<<i<<": ";
		printf("%.7lf\n",time);
	}
	return 0;
} 
