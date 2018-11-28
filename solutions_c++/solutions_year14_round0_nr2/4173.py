#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

#define MIN(a,b) ((a)>(b)?(b):(a))

/*
int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	in.open("test.txt");
	out.open("out.txt");
	in>>CaseNum;
	for(int Case=0;Case<CaseNum;Case++){



	out<<"Case #"<<Case+1<<":";
	}
	return 0;
}
*/

double F0;

double f(double st,double C,double F,double X){
	if(st>=X)return 0;
	if(st<C&&X<=C)return (X-st)/F;
	if(st<C&&X>C)return (C-st)/F+f(C,C,F,X);
	if(X<=F/F0*C+st)return (X-st)/F;
	return f(st-C,C,F+F0,X);
	

}

int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	//in.open("test.txt");
	in.open("B-small-attempt0.in");
	out.open("out.txt");
	in>>CaseNum;
	double C,X;
	double t;
	out.setf( std::ios::fixed, std:: ios::floatfield );
	out.precision(7);

	for(int Case=0;Case<CaseNum;Case++){
		in>>C>>F0>>X;
		t=f(0,C,2,X);




	out<<"Case #"<<Case+1<<": "<<t<<endl;
	}
	return 0;
}

