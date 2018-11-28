#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

ofstream fout("cookie.out");

int T;
double C;//cost of a farm
double F;//rate if cookie production of the farm
double X;//final goal
//end of input variables

double ccount=0.0;//cookie count
double total_time=0.0;//total
double rate=2.0;

int main(){
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>C>>F>>X;
		ccount=0.0;
		total_time=0.0;//total
		rate=2.0;
		while(ccount<X){
			float op1_val=(X-ccount)/rate;//not buying a cookie farm
			float op2_val=(C-ccount)/rate+ X/(rate+F);//buying a cookie farm
			if(op1_val <= op2_val){
				ccount=X;
				total_time+=op1_val;
				//no change in rates
			}else{
				total_time+=(C-ccount)/rate;
				ccount=0;
				rate+=F;
			}
		}
		fout<<"Case #"<<i<<": "<<fixed<<setprecision(8)<<total_time<<endl;
	}
	return 0;
}