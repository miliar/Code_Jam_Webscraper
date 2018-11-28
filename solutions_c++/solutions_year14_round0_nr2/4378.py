#include<iostream>
#include<stdio.h>
#include<iomanip>

using namespace std;

int main(){
int T;
cin>>T;
for(int i=1; i<=T; i++){
	double C, F, X, time=0, rate=2;
	cin>>C>>F>>X;
	while(true){
	float time1=(C/rate)+(X/(rate+F));
	float time2=(X/rate);  
	if(time1<time2){
		time+=C/rate;
		rate+=F;
	}
	else break;
	}
	time+=(X/rate);
	cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<time<<endl;
}
}
