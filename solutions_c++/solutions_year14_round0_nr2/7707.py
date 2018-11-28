#include <iostream>
#include <iomanip>

using namespace std;

void solve(double c, double f, double x) {
	long double prev, sum;
	long double sprev = 0;
	long double cur = x / 2;
	int i = 0;

	do {
		prev = cur;
		sum = sprev + c / (2 + i*f);
		sprev = sum;
		cur = x / (2 + (i + 1)*f) + sum;
		i++;
	} while(cur < prev);

	cout <<fixed <<setprecision(15) <<prev <<endl;
}

int main() {
	// freopen("in.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);
	int T;

	cin >>T;

	for(int t = 0; t < T; t++) {
		double c, f, x;
		cin >>c >>f >>x; 
		cout <<"Case #" <<t + 1 <<": ";
		solve(c, f, x);
	}
	return 0;
}