#include<iostream>
#include<map>
#include<cmath>
#include<cstring>
#include<iomanip>
using namespace std;



int main(){
	int t,first,second;
	
	cin>>t;
	int cases=0;
	double C,F,X;
	
	while(t--){ 
	    cases++;
		cin>>C>>F>>X;
		double time=0.0;
		double rate=2.0;
		while((X/(double)rate)>((C/double(rate))+X/(double)(rate+F))){
			time+=C/double(rate);
			rate+=F;
		}
		time+=X/(double(rate));
		cout <<"Case #"<<cases<<": ";
		printf("%.7lf\n", time);
		
		
		
		
		
		
		
		
		
	}
	
	
	
	return 0;
	
	
}