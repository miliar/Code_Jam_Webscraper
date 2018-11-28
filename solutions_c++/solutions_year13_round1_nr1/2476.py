#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cfloat>
using namespace std;

int T;
vector<vector<int> > grid2D (5, vector<int>(5));
vector<int> grid1D(5) ; 
int i;
int j;
int k;
double r;
double z;
double paint;
unsigned long long answer;
double s;
unsigned long long m;
double b2;
double bb2;
double fac;
double sb2fac;
double q;
int main(int argc, char *argv[]) {
	ifstream in("A-small-attempt0.in");
	in>>T;

	ofstream out("A-small-attempt0.out");
	for(i=1;i<=T;i++){
	
			in>>r;
			in>>paint;
			b2=2*r;
			m=b2;
			m=m-1;
			bb2=4*r*r-4*r+1;
			fac=8*paint;
			q=bb2+fac;
			sb2fac=pow(q,.5);
			s=sb2fac;
			//answer=s;
			answer=s-r-r+1;
			answer=answer/4;
			out << "Case #" << i << ": " <<answer<< endl;

	}
	return 0;
}

