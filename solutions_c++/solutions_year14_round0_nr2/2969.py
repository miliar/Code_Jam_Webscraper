#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void solve(int N)
{
	double C, F, X;
	cin >> C >> F >> X;
	double cps = 2; //default cps;
	double time = 0;
	while (true) {
		double winTime = time + X / cps;
		double farmTime = time + C / cps;
		double farmWinTime = farmTime + X / (cps + F);
		if (winTime < farmWinTime) {
			cout << winTime;
			break;
		}
		time = farmTime;
		cps += F;
	}
}

int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}

	return 0;
}