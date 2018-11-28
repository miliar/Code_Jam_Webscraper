#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <cmath>

using namespace std;

void solve() {
	int P, Q;
	cin >> P;
	cin.ignore(1);
	cin >> Q;
	double power = log2(Q);
	if(power == round(power) && P % 2 == 1) {

		int counter = 1;

		while(P < Q/2) {
			Q/=2;
			counter++;
		}
		cout << counter;

	} else {
		cout << "impossible";
	}
}

int main()
{
	int T; cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
