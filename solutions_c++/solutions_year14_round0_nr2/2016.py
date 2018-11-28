#include<iostream>
#include<string>
#include<set>
using namespace std;

int main(){
	int T; cin>>T;
	cout.setf(ios::fixed);
	cout.precision(7);
	for(int kases=1;kases<=T;kases++){
		double C,F,X;
		cin>>C>>F>>X;
		double cP = 2.0,nP = 2.0+F;
		double res = 0.0 ;
	
		while( X/cP > (C/cP + X/nP) ){
			res += C/cP;
			cP = nP; 
			nP += F;
		}
		res += X/cP;
	
		cout<<"Case #"<<kases<<": "<<res<<endl;
	}
}
