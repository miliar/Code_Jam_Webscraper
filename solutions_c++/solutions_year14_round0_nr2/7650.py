#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("B-large.in");
    freopen("output","w",stdout);
	int T, seq = 1;
	double C, F, X, res;
	in >> T;
	while(seq <= T) {
		in >> C >> F >> X;
		if (X <= C)
			res = X/2.0;
		else {
			double v = 2.0;
			res = 0;
			while(X/v > (C/v + X/(v+F))) {
				res += C/v;
				v += F;
			}
			res += X/v;
		}
		printf("Case #%d: %.7lf\n", seq++, res);
	}
    return 0;
}
