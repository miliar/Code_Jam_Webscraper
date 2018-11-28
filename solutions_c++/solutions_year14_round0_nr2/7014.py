#include <iostream>
#include <stdio.h>
using namespace std;

double timetoobjective(double x, double prod){
	return x/prod;
}

double timetofarm(double c, double prod){
	return c/prod;
}
double temps(double c, double f, double x){
	double rentabilite = c/f;
	double prod = 2.0;
	double time=0.0;
	while(timetoobjective(x,prod)>timetofarm(c,prod)+rentabilite){
		time+=timetofarm(c,prod);
		prod+=f;
	}
	time+=timetoobjective(x,prod);
	return time;
}

int main(){
	int T;
	cin >> T;
	for(int k=1;k<=T;++k){
		double c,f,x;
		cin >> c >> f >> x;
		//cout << "Case #" << k << ": " << temps(c,f,x) << endl;
		printf("Case #%d: %.8f\n",k,temps(c,f,x));
	}
}
