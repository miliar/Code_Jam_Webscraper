#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<fstream>
#include<iomanip>
using namespace std;
double fn(double co, double prof, double req, double cur) {
	if((req/cur) > ((co/cur) + (req/(cur+prof)))) {
		return min(req/cur, co/cur + fn(co,prof,req,cur+prof));
	} else {
		return req/cur;
	}
}
int main() {
	fstream f;
	fstream x;
	f.open("B-small-attempt0.in",ios::in);
	x.open("output.txt",ios::out);
	int t;
	f>>t;
	for(int i=1;i<=t;i++) {
		double co,prof,req;
		f>>co>>prof>>req;
		double sol = 0.0;
		if(req<=co) {
			sol = req/2.0;
		} else {
			sol = req/2.0;
			sol = min(sol, co/2.0 +fn(co,prof,req,2.0+prof));
		}		
	//	printf("Case #%d: %.8lf\n",i,sol);
		x<<"Case #"<<i<<": "<<fixed<<setprecision(10)<<sol<<"\n";
	}
	f.close();
	x.close();
	return 0;
}
