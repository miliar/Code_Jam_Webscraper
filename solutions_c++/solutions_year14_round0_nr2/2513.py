#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;


int main(){
	int T,t=1;
	double C , F, X , P , newF = 0 ,oldF= 0 , calSum1 , calSum2;
	cin>>T;
	for(t = 1 ;t<=T ; t++){
		cin>>C>>F>>X;

		calSum1 =X/2.0; //2000
		calSum2 =  C/2.0 +  X/(F+2.0); // 583
		
		newF = F + 2.0;
		while(calSum1 > calSum2){
			
			calSum1 = calSum2; //583
			oldF = newF;
			newF = F + newF;			
			calSum2 = calSum1 - X/oldF + (C/oldF + X/newF); // 533
		}
		
		if(calSum1 > calSum2){
			//cout<<setprecision(10);
			//cout<<"Case #"<<t<<": "<<calSum2<<"\n";
			printf("Case #%d: %.7lf\n",t,calSum2);
		}
		else{
			//cout<<setprecision(7);
			//cout<<"Case #"<<t<<": "<<calSum1<<"\n";
				printf("Case #%d: %.7lf\n",t,calSum1);
		} 
	}
	return 0;
}
	
