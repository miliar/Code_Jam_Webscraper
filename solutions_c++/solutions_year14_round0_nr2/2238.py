#include <iostream>
#include <iomanip>
using namespace std;

double C,F,X,r;

double cca(double r){

	double t1=X/r;

	double dt=C/r;

	double t2=dt+X/(r+F);

	if (t1<=t2) return t1;

	return dt+cca(r+F);
	
}

int main(){
	int T;
	cin>>T;

	cout<<fixed<<setprecision(7);

	for (int i=1;i<=T;i++){
		cin>>C>>F>>X;
		r=2.0;

		cout<<"Case #"<<i<<": "<<cca(r)<<endl;
	}

	return 0;
}
