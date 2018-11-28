#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main(void){
	int T;
	double C,F,X;
	ifstream cin("B-large (1).in");
	ofstream cout("2014_gcj_qr_B.out");
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> C >> F >> X;
		double te = 0.0;
		if(C>=X)te = X/2.0;
		double ex = 2.0;
		while(C<X){
			if(X/ex <=(C/ex+X/(ex+F))){
				te += X/ex;
				break;
			}
			else{
				te+=C/ex;
				ex+=F;
			}
		}
		cout << "Case #"<<(i+1)<<": ";
		cout <<setprecision(7)<<fixed<<te<<endl;
	}
	system("pause");
}