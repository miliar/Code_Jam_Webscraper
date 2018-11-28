#include <iostream>
#include <iomanip> 
using namespace std;

int nCases;
double C;
double F;
double X;
double V;

#define N 1000000

bool shouldBuyFarm(double V){
	if ( V*C > F*(X-C)){
		return false;
	}
	return true;
}
int main(){
	int index  = 1;
	
	cin>>nCases;
	while( nCases--){
		cin>>C>>F>>X;
		V = 2.0;
		double time = 0;
		while( shouldBuyFarm(V)){
			//buy farm;
			time += (N * C)/V;
			V += F;
		}
		time += (N * X)/V;
		cout<<"Case #"<<index<<": ";
		index++;
		cout <<fixed<<setprecision(7)<<time/N<<endl;
		
		
	}
	return 0;
}
