#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int n;
	double c,f,x;
	cin>>n;
	cout << fixed;
	for(int num=1; num<=n; ++num){
		cin>>c>>f>>x;
		double rate=2;
		double t=0;
		double total=0;
		while(total<x){
			if(total<c){
				total=c;
				t+=c/rate;
			}
			if( (c/f) < (x-c)/rate ){
				total -= c;
				rate += f;
			}
			else{
				t += (x-c)/rate;
				total = x;
			}
		}

		cout<<setprecision(7)<<"Case #"<<num<<": "<< t <<endl;

	}
}