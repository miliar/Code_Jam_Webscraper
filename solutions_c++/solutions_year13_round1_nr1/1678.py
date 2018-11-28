#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <sstream>



using namespace std;

const double PI = 3.14159265359;

double area(int r) {
	return (r+1)*(r+1) - r*r;
}

int main(){

	int tests, r;
	double t;
	cin >> tests;
	int c = 1;
	while (tests--) {

		cin >> r >> t;
		int res = 0;
		while (t >= area(r)){
			res++;
			t -= area(r);
			r += 2;
		}
	cout << "Case #" << c << ": " << res << endl;
	c++;
	}
}