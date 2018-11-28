#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
 
#define PI 3.14159265358979
 
using namespace std;
typedef unsigned long long ull;

int min (int a,int b) {
	return a<b?a:b;
}

int max (int a,int b) {
	return a>b?a:b;
}

//vector <int> (,0);


int main()
{
	FILE * in=fopen("D:\\dev\\VPW\\problem 4\\p4\\p4\\B-large.in","r");
	FILE * out=fopen("D:\\dev\\VPW\\problem 4\\p4\\p4\\A-out.out","w");
	int t;
	fscanf(in,"%d",&t);
	for (int i=0;i<t;i++) {
		double C,F,X;
		fscanf(in,"%lf %lf %lf",&C,&F,&X);
		double ksol=0;
		for (double k=0;;k++) {
			if ((X-C)/(2.0+k*F) < X / (2.0+(k+1.0)*F)) {
				ksol=k;
				break;
			}
		}

		double sol=0;
		for (double k=0;k<ksol;k++) {
			sol+=C/(2.0+k*F);
		}
		sol+=X/(2.0+(ksol)*F);
		fprintf(out,"Case #%d: %lf\n",i+1,sol);
	}

	
	
	fclose(in);fclose(out);
    return 0;
}