#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

void test(int i) {
	double C, F, X;
	cin >> C >> F >> X;
	double R = X / 2.0;
	double T = C / 2.0;
	for(int j=1; 1; j++) {
		double T2 = T + X/(2.0 + j * F);
		if(T2 > R) break;
		R = T2;
		T = T + C/(2.0 + j * F);
	}
	cout << "Case #" << i << ": " << fixed << setprecision(7) << R << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int n; cin >> n;
	for(int i=1; i<=n; i++) test(i);
	fclose(stdin);
	fclose(stdout);
	return 0;
}
