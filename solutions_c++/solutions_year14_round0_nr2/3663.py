#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

int main(){
	int cases,tmp=1;
	cin>>cases;
	while(cases>0){
		double goal,cost,increase,gen=2,time;
		cin>>cost>>increase>>goal;
		double a=(goal/gen);
		double fac=(cost/gen);
		double b=a;
		for(double i=1;a>=b;i++){
			a=b;
			b=fac+(goal/(increase*i+gen));
			fac=fac+(cost/(increase*i+gen));
		}
		cout<<"Case #"<<tmp<<": "<<std::setprecision(10)<<a<<endl;
		cases--;tmp++;
	}
}
