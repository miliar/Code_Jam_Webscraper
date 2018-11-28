/*************************************************************************
    > File Name: B.cpp
    > Author: csy
    > Mail: chshaoyi7@gmail.com 
    > Created Time: 2014年04月12日 星期六 14时33分03秒
 ************************************************************************/

#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

#include<fstream>

#define eps 0.00000001

int Ceil(double number){
	

	if(number < 0) return 0;
	return (int)(ceil(number));
}


double Cal(double X,double F, double C, int n){
	double result = 0;	
	for(int j = 0; j <= n; j ++)
		result += C/(2.0 + F * double(j));
	
	result += X / (2.0 + F * (double)(n + 1));

	return result;
}

int main(){
	
	ifstream fin("BLarge.in");
	ofstream fout("BLarge.out");

	int t;
    double C,F,X;
	double fvalue;
	double result;
	int n;
	fin >> t;

	for(int i = 1; i <= t; i ++){
		fin >> C >> F >> X;
		
		fvalue = X / C - 2 / F - 2;


		result = X / 2.0;

		n = Ceil(fvalue);

		for(int j = -1; j <= 1; j ++){
			double temp = Cal(X,F,C,n + j);
			if(temp < result) result = temp;
		}


		
	    fout << setprecision(7) << setiosflags(ios::fixed | ios::showpoint)<<"Case #" << i << ": " << result << endl;

	}

	return 0;
}
