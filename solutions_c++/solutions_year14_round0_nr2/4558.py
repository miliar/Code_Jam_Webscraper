#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <set>
#include <cstring>
#include <cassert>

#define F(i, a,b) for(int i=int(a);i<int(b);i++)
#define foreach(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)
#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;

#define L long long
using namespace std;

int cases = 1;
double getf(double f0, double r, int n) {
	return f0 + (double)(n-1) * r;
}

double ff(double i, double f, double x, double c) {
	double seg = 0.0;
		for(int j = 1; j < (int)i; j++) {
			seg = seg + c / getf(2.0, f, j);
		}
	double resNext = x / getf(2.0 ,f, i) + seg;
	return resNext;
}

//464.69104 3.65643 84.09680

void resolve2() {
	double c,f,x;
	scanf("%lf%lf%lf",&c, &f, &x);

	double l = 0.0, r = 100000.0, EPS = 0.000001; // input
	while (r - l > EPS) {
	   double m1 = l + (r - l) / 3,
	 	 m2 = r - (r - l) / 3;

	 	 double a = ff (m1, f, x, c);
	 	 double b = ff (m2, f, x, c);
		 // cout << ff (m1, f, x, c) << ", " << ff (m2, f, x, c) << endl;
	 	 // cout << r << ", " << r << endl;
	 	 if(b <= 0)  break;
	   if (a > b) // f - convex function
	      l = m1;
	   else
	      r = m2;
	}
	
	printf("Case #%d: %.7lf\n", cases++, ff(r, f, x, c));
	//cout << "************" << endl;
}
void resolve() {
	double c,f,x;
	scanf("%lf%lf%lf",&c, &f, &x);
	double resAnt = x/2.0;
	F(i,1,100000) {
		double seg = 0.0;
		F(j,1,i) {
			seg = seg + c / getf(2.0, f, j);
		}
		double resNext = x / getf(2.0 ,f, i) + seg;

		if(resNext > resAnt) {
			printf("Case #%d: %.7lf\n", cases++, resAnt);
			//cout << "*******" << endl;
			return;	
		}

		resAnt = resNext;

		// cout << x / getf(2,f,i) + seg << endl;
	}
	

}	

int main() {
	int t;
	scanf("%d", &t);
	F(i,0,t) {
		resolve2();
	}
}