#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

void solve(double costFarm, double farmProd, double xWin)
{
	double prod, secs, thisone;
	double nt_prod, nt_secs, nt_thisone;
	double totalSecs = 0.0;
	int nf = 0;

	for(;;) {
		prod = farmProd * nf + 2;
		secs = costFarm / prod;
		thisone = xWin / prod;

		nt_prod = farmProd * (nf+1) + 2;
		nt_secs = costFarm / nt_prod;
		nt_thisone = xWin / nt_prod;

		if(totalSecs + thisone < totalSecs + secs + nt_thisone) {
			totalSecs += thisone;
			break;
		}

		totalSecs += secs;
		nf++;
	}

	cout << fixed << setprecision(7) << totalSecs;
}

int main()
{
	double c, f, x;
	int numCases = 0;
	cin >> numCases;

	for(int i=0; i < numCases; i++) {
		cin >> c >> f >> x;

		cout << "Case #" << i+1 << ": ";
		solve(c, f, x);
		cout << endl;
	}
	return 0;
}
