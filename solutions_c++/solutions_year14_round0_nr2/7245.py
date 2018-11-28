// google.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>
#include<fstream>
#include<iomanip>


using namespace std;

//#include "stdlib.h"

int main(int argc, char* argv[])
{
	FILE *fp;
//	FILE *out;
	if( (fp=fopen("B-large.in","r" ))==NULL )
		cout<<"\n不能打开in文件" <<endl;
	ofstream fout("B-large.out");

	double T;
	int m;
	double C,F,X;
	double farmT=0;
	double ckT=0;
//	int cookies=0;
	double pre,now;
	double rate;
	double max,min;
	
	fscanf(fp,"%lf",&T);
//	cout << T;
	for(m=0;m<T;m++)
	{
		fscanf(fp,"%lf",&C);
		fscanf(fp,"%lf",&F);
		fscanf(fp,"%lf",&X);
//		cout << C<<" " << F<<" " << X<< endl;
		pre=now=0;
		rate=2;
		farmT=0;
		now=pre=X/rate;
//		cout << "pre:" <<pre << "now" << now << endl; 
		while(now <= pre)
		{
			pre = now ; 
//			cout << "pre:" <<pre << "now" << now << endl; 
			farmT+=(C/rate);
			ckT=X/(rate+F);
			now=farmT+ckT;
			rate+=F;
		}
//		cout <<setprecision(1) << 6.0 <<endl; cout<<setw(3)<<setfill('0')<<a<<endl;
	//	printf("Case #%d: ",m);
		cout.setf(ios::fixed); 
		fout <<"Case #" << m+1 <<": " <<setprecision(7) << pre<<endl;
	//	fout<<"Case #"<<m+1 <<": "<<pre<<endl;
	}
	return 0;
}
