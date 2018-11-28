#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}

	int T;
	cin >> T;
	cout.precision(15);
	for (int i = 1; i <= T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double c = 2;
		double t = 0;
		for(;;) {
			const double wt = X / c + t;
			const double ft = C / c + t;
			const double fwt = X / (c + F) + ft;
			if (wt < fwt) {
				cout << "Case #" << i << ": " << wt << endl;
				break;
			}
			t = ft;
			c += F;
		}
	}

	return 0;
}