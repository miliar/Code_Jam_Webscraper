#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;

int main(){

int t;
cin>>t;
std::cout << std::fixed;
std::cout << setprecision(7);
int k=1;
	while(k<=t){

	double c,f,x;
	cin>>c>>f>>x;
	double ini=0;
	double sec=0;
	double rate=2;
	while(ini!=x){
		double r1=(x)/rate;
		double r2=(c)/rate + x/(rate+f);
//		cout<<"hi"<<r1<<" "<<r2<<endl;		
		if(r1<=r2) { sec+=r1; break;}
		else { sec+=(c)/rate; rate+=f;}
//		cout<<"sec"<<sec<<endl;

	}
		cout<<"Case #"<<k<<": "<<sec<<endl;	
		++k;
	}

}

