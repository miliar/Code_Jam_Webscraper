#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	freopen("cookie.in", "r", stdin);
	freopen("cookie.out", "w", stdout);
	
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		double C, F, X, cps = 2, tot = 0;
		cin >> C >> F >> X;
		cout << "Case #" << (i+1) << ": ";
		while (1) { //god, I hate using infinite while loops
			if (X/cps+tot < C/cps+tot+X/(cps+F)) {
				cout << setprecision(10) << X/cps+tot;
				break;
			}
			tot += C/cps;
			cps += F;
		}
		cout << "\n";
	}
	return 0;
}
