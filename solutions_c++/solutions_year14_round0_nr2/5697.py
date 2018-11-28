#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;


double lulz(double T, double r, double C, double F, double X, double lim, int i) {
	if (T > lim || i == 2000) return 1000000;
	double c1,c2;

	c1 = X/r;

	c2 = C/r + lulz(T+C/r, r+F, C, F, X, lim, i+1);

	return min(c1,c2);

}

int main() {

	int T;
	cin >> T;
	ofstream out("CookieClicker.txt");
	for (int idx = 1; idx <= T; idx++) {
		double T = 0.0, r = 2.0, C, F, X,ans;
		cin >> C >> F >> X;

		ans = lulz(T,r,C,F,X,X/r,0);
		out << fixed << showpoint << setprecision(7);
		out << "Case #" << idx << ": " << ans << endl;

	}
	out.close();
	return 0;
}