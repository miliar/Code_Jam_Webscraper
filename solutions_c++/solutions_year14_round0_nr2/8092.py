#include<iostream>
#include<iomanip>
using namespace std;
int main() {
	int T;
	cin>>T;
	double C, F, X;
	for(int i=0;i<T;++i){
		double timeWithoutFarm = 0;
		double totalTime = 0;
		double timeWithFarm = 0;
		double cookieGenerator = 2;
		cin>>C>>F>>X;
		do{
		double temp1 = C/cookieGenerator;
		timeWithoutFarm = X/cookieGenerator;
		timeWithFarm = temp1 + X/(cookieGenerator + F);
		if(timeWithFarm<timeWithoutFarm) {
			totalTime += temp1;
			cookieGenerator += F;
		}
		else{
			totalTime += timeWithoutFarm;
		}
		}while(timeWithFarm<timeWithoutFarm);
		cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<totalTime<<"\n";
	}
}
