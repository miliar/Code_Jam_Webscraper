#include <iostream>
#include <algorithm>    // std::sort
#include <vector>  
#include <stdio.h>
using namespace std;

void solve()
{
	double C, F, X;

	cin >> C >> F >> X;

	double min_t, t;

	min_t = X/2.0;

	for (int i=1; i<=X/C; i++) {
		t = 0;
		for (int j=0; j<i; j++) {
			t += C/(F*j+2);
		}
		t += X/(F*i+2);
		if (t < min_t) {
			min_t = t;
		}
	}

	printf("%.7f", min_t);

	return;
}

int main() {
	int T;

	cin >> T;

	for (int i=1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	// your code goes here
	return 0;
}
