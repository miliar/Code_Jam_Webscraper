/*
 * cookie.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: lav
 */



/*
 * magic.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: lav
 */



#include<stdio.h>
#include<iostream>
#include<fstream>
#include <iomanip>


using namespace std;
double get_time(int n,double C,double F, double X);
		int main(){

			ifstream infile;
			ofstream outfile;
			outfile.open("a.out");
			outfile << std::fixed << setprecision(7);
	infile.open("a.in");
	int t;
		infile>>t;

	for(int tt=0;tt<t;tt++){

		double C,F,X;
		infile>>C>>F>>X;


		double cur_time=X/2;
		double ti;
		for(int n=0;;n++){
			ti=get_time(n, C, F, X);
			if(tt==1)
			cout<<get_time(n, C, F, X)<<"\n";
			if(ti>cur_time){ break;}
			else cur_time=ti;
		}
		outfile<<"Case #"<<tt+1<<": "<<cur_time<<"\n";

	}
outfile.close();

		}
double get_time(int n,double C,double F, double X){
	double t=0;
	if(n==0) return X/2;
	for(int i=0;i<n;i++){
		t+=C/(2+(i*F));
	}
t+=(X)/(2+n*F);
	return t;

}
