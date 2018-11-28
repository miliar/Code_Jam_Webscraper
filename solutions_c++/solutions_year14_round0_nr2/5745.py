#include <iostream>
using namespace std;

double mintime(double &C , double &F , double &X , double rate){
	if(((X/rate - ( C/rate + C/(rate+F)) ) < 0.1) || (X/rate < ( C/rate + C/(rate+F)))) {
		return X/rate;
	}
	double mtime=C/rate + mintime(C,F,X,rate+F);
	if(X/rate < mtime){
		return X/rate;
	} else {
		return mtime;
	}
}

int main(void) {
	cout.precision(10);
	int T ;
	double C , F , X ,  rate=2;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>C>>F>>X;
		cout<<"Case #"<<t<<": "<<mintime(C,F,X,rate)<<endl;
		
	}
	return 0;
}
