#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

int upper(double X,double C){
	
	return int(X/C)+1;
}

double calc_time(double cur_sp,int cur_farms,const int max_farms,const double C,const double F,const double X){
	if(cur_farms<max_farms)
	return C/cur_sp+calc_time(cur_sp+F,cur_farms+1,max_farms,C,F,X);
	else
	return X/cur_sp;
}

double one_case(){
	double C=0,F=0,X=0;
	
	cin>>C>>F>>X;
	double best = X/2.0;
	
	for(int i=0;i<upper(X,C);i++){

		double tmp = calc_time(2.0,0,i,C,F,X);
		//cout<<fixed<<setprecision(7)<<i<<": "<<tmp<<endl;
		if(best-tmp>0.000001)
			best = tmp;
	}
	
	return best;
}

int main(){
	int tests = 0;
	cin>>tests;
	ofstream fout;
	fout.open("_gcj_q2.out");
	
	for(int i=0;i<tests;i++){
		fout<<"Case #"<<i+1<<": ";
		fout<<fixed<<setprecision(7)<<one_case();
		fout<<endl;
	}
}