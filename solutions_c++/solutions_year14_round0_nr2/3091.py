#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;

int main (int argc,char* argv[]){
	ifstream is(argv[1]);
	ofstream os(argv[2]);
	int cases ;
	is >> cases ;
	long double T = 0.0;
	long double c ;
	long double f ;
	long double x ;	
	long double rate = 2.0 ;
	for(int i=0;i<cases;i++){
		is >> c ;
		is >> f ;
		is >> x ;
		while(x/rate > (c/rate + x/(rate+f))){
			T+= c/rate ;
			rate = rate + f ;
		}
		T+=x/rate ;
		os<<"Case #"<<fixed<<setprecision(7)<<i+1<<": "<<T<<endl ;
		T = 0.0 ;
		rate = 2.0 ; 
	}
	
	
	
	
	
	
	
}
