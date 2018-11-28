#include <iostream>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
using namespace std;

void tst()
{
	long long r,t;
	cin >> r;
	cin >> t;

	if (2*r+1 > t) {
		cout << 0;
		return;
	}

//	double log_t = log10((double)t);
//	cout << log_t << "\t";
	long long min_y = 1;
	long long  max_y = (long long)sqrt(t);
//	double log_y, log_yr;
	long long y = (min_y+max_y)/2;
	while (1) {
//		log_y = log10((double)y);
//		log_yr = log10((double)(y*2+r*2-1));
//		cout << "y+yr:" << y*(y*2+r*2-1) << "y:" << y << "\t";
		//if (log_y+log_yr < log_t) {
		//	min_y = y;
		//} else 
//		if (log_y+log_yr > log_t) {
		if ((y*2+r*2-1) > (double)t/y) {
//			cout << "LARGE " << y*(y*2+r*2-1) << "y:" << y << "\t";
			max_y = y;
		} else {
//			cout << "SMALL " << y*(y*2+r*2-1) << "y:" << y << "\t";
			min_y = y;
			//cout << y;
		//	return;
		}
		y = (min_y+max_y)/2;
		if (y == min_y || y == max_y) {
			cout << min_y;
			return;
		}
	}

	return;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		tst();
		cout << endl;
	}
}



