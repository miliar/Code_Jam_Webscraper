#include <iostream>
#include <cmath>
using namespace std;
#define BILLION 1000000000
typedef long long LL;

LL r, t;

LL f(LL n) {
	return 2*n*n + n*(2*r-1);
}

int g() {
	double b = (2*r-1);
	double c = 2 * 1e18;
	double x = (-b + sqrt(b*b+8*c)) / 4;
	return (int)x;
}

int binsearch(int a, int b) {
	//cout << a << " " << b << endl;
	if (a == b)
		return a;
	int m = 1 + (a+b)/2;
	//cout << "f(m) = " << f(m) << " t = " << t <<  endl;
	if (f(m) > t)
		return binsearch(a, m-1);
	else
		return binsearch(m, b);
}	

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> r >> t;
		LL res = binsearch(1, g());
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
