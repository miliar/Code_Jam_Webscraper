//
//  main.cpp
//  jam1
//
//  Created by Vipul Verma on 12/04/14.
//  Copyright (c) 2014 Vipul Verma. All rights reserved.
//


#include <iostream>
#include <cstdio>
using namespace std;
double calculate(double C, double F, double X)
{
	double cp = 2.0;
	double seconds = 0;
	double temp = 1000000000.0;
    
	for (int j = 0; j < 100000; ++j)
	{
		double tmp = seconds + (X /cp);
		temp = min(tmp, temp);
		seconds += C / cp;
		cp += F;
	}
	return temp;
}
int main()
{
    FILE *fin=fopen("B-large.in","r");
    FILE *fout=fopen("B-large.out","w");
    int t,k=1;
    double  c, f, x;
	fscanf(fin,"%d",&t);
	cout.precision(15);
	while(t--)
    {
		fscanf(fin,"%lf%lf%lf",&c,&f,&x);
		fprintf(fout,"Case #%d: %lf\n",k,calculate(c, f, x));
        k++;
    }
	return 0;
}
