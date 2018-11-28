#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

bool fair(int i) {
	if (i==1000) return false;
	if (i<10) return true;
	int a3 = i/100;
	int ii = i-a3*100;
	int a2 = ii/10;
	int a1 = ii-a2*10;
	if (a1==a3) return true;
	if (a3==0 && a1==a2) return true;
	return false;
}

bool square(int i) {
	int j = sqrt(i+0.01);
	return j*j==i && fair(j);
}

int main() {
	int T, A, B;
	cin >> T;

	for (int t=1; t<=T; t++) {
		cin >> A >> B;
		int count = 0;
		for (int i=A; i<=B; i++)
			if (fair(i) && square(i)) count++;
		cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}


