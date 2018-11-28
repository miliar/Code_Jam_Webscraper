#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large-output.txt", "w", stdout);
	int T, i;
	double C, F, X;
	double time;
	double t, farmCost;
	int n=0;

	cin >> T;
	for (i = 1; i <= T; i++) {
		n = 0;
		cin >> C >> F >> X;
		cout << "Case #" << i << ": ";
		time = X / 2;
		farmCost = C / 2;
		t = farmCost + (X / (2 + F)); 
		n++;
		while (time > t) {
			time = t;
			farmCost += C / (2 + n*F);	
			n++;
			t = farmCost + X / (2 + n*F);
		}
		cout.precision(7);
		cout <<fixed<< time << endl;
 
	}

	fcloseall();
}