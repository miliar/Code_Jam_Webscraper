#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
	int T;
	cin >> T;
	double C, F, X, final;
	for (int i = 1; i <= T; i++) {
		double minimo = 18446744073709551615.0;
		cin >> C >> F >> X;
		cout << "Case #" << i << ": ";
		double acum = C / 2;
		double y = X / 2;
		minimo = y;
		double j = 1.0;
		while (1) {
			y = X / (F * j + 2);
			final = y + acum;
			if (final > minimo) {
				printf("%.7f\n", minimo);
				break;
			} else {
				minimo = final;
			}
			acum = acum + (C / (F * j + 2)) ;
			j = j + 1.0;
		}
	}
	return 0;
}
