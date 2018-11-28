#include<stdio.h>
#include<iostream> 
#include<fstream>   
using namespace std; 
int main()  
{  
    ifstream cin("a.in");
    freopen("a.out","w",stdout);
	int T, cas;
	double C, F, X, i, v, count, res, min;
	cin >> T;
	for (cas = 1; cas <= T; cas++) {
		cin >> C >> F >> X;
		if (X <= C)
			res = X/2;
		else {
			v = 2.0;
			res = 0;
			while(X/v > (C/v + X/(v+F))) {
				res += C/v;
				v += F;
			}
			res += X/v;
		}
		printf("Case #%d: %.7lf\n", cas, res);
	}
    return 0;  
}  
