//#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#define N 9000
using namespace std;

int main()
{
	long double C, F, X; 
	int ii,j,testn, id;	

	//int r1, r2, arr1[N][N]={0}, arr2[N][N]={0};
	long double s[N] ={0}, t1[N] = {0}, t1c[N] = {0}, t2[N] = {0}, ss[N] = {0};	
	double minv;
	ifstream readfile ;
	readfile.open("ab.in");
	readfile >> testn;
	
	//cin >> testn;
	long double* val = new long double[testn];
	ofstream myfile;
	myfile.open ("qq.txt");
	
	for(ii=0; ii<testn; ii++)
	{		
		//s =0, t1 = 0, t1c = 0, t2 = 0, ss = 0;	
		readfile >> C;
		readfile >> F;
		readfile >> X;		
		
		for(j=0;j<N;j++) {			
				s[j] = 2 + j*F; 
				t1[j] = C/s[j];
				//t1c[j] += t1[j];
				t2[j] = X/s[j];
		}
		t1c[0] = t1[0];
		for(j=1;j<N;j++) {				
				t1c[j] = t1c[j-1] + t1[j];
				
		}
		//cout << "here" << endl;
		
		ss[0] = t2[0];
		for(j=1;j<N;j++) {			
				ss[j] = t2[j] + t1c[j-1];			
		}
		//cout << "here2" << endl;
		

		minv = ss[N-1];
		id = N-1;
		if (X <= C) {
			val[ii] = X/2;
		}
		else {
		for(j=0;j<N;j++) {			
				if(ss[j] < minv)
				{
					minv = ss[j];
					id = j;					
				}			
		}	
		val[ii] = ss[id];
		}
		//cout << "value " << ss[id] << endl;
		
	}

	for(ii=0;ii<testn;ii++)
	{		
		myfile << "Case #" << ii+1 << ": "  << setprecision(10) << val[ii] << endl;
		//cout << "output " << setprecision(10) << val[ii] << endl;
		
	}
	myfile.close();
	return(0);
}
