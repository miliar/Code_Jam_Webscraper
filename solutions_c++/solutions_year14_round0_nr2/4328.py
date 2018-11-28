#include <iostream>
#include <iomanip>
using namespace std;

double time(double X , double rate){
	return X/rate;
}

double timec(double X , double ratei , double rate , double factmoney){
		double t,td;
		t = time(X,ratei);
		td = time(factmoney,ratei) + time(X,ratei + rate);
		if(td < t)
			return time(factmoney,ratei) + timec(X,ratei + rate,rate,factmoney);
		else
			return t;
}

int main(){
	int testc;
	cin >> testc;
	for(int i = 1 ; i <= testc ; i++){
		double X,rate,factmoney;
		cin >> factmoney >> rate >> X;
		cout.precision(7);
		cout.setf( ios::fixed, ios::floatfield );
		cout << "Case #" << i << ": " << timec(X,2,rate,factmoney);
		cout << endl;
	}
}
		
	
