#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned int unint;

double minimum_time(double C, double F, double X, double S, double P){
	double s1 = C/P, s2 = X/P, s3 = X/(P+F);
	if(s1+s3>s2) return S + s2;
	return min(minimum_time(C,F,X,S+s1,P+F),s2+S);
}

int main(int argc, char *argv[]) {
	unint T,i=1;
	double C,F,X;
	cin>>T;
	cout.precision(7);
	cout<<fixed;
	while(i<=T){
		cin>> C >> F >> X;
		cout<<"Case #"<<i++<<": " << minimum_time(C,F,X,0,2) <<endl;
	}
	return 0;
}

