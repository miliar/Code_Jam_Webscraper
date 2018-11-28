#include <cstdio>
#include <iostream>

using namespace std;


double s(double c, double f, double x, int n) {
	double time = 0;
	double rate = 2.0;
	for(int i = 0; i < n; ++i) {
		time += (c / rate);
		rate += f;
	}
	time += x / rate;
	return time;
}
void solve(int t) {
	double c, f, x;
	cin >> c >> f >> x;
	double result = 0;
	
	int low = 0, high = 100000;
	while(low <= high) {
		int mid = (low + high) >> 1;
		int left = mid - 1;
		int right = mid + 1;
		double mid_val = s(c, f, x, mid);
		double left_val = left < 0 ? mid_val : s(c, f, x, left);
		double right_val = right > 100000 ? mid_val : s(c, f, x, right);
		result = mid_val;
		if(left_val <= mid_val and mid_val <= right_val) {
			high = mid - 1;
		}
		else if(left_val >= mid_val and mid_val >= right_val) {
			low = mid + 1;
		}
		else {
			break;
		}
	}
	
	printf("Case #%d: %.7lf\n", t+1, result);
}
int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		solve(i);
	}
	return 0;
}