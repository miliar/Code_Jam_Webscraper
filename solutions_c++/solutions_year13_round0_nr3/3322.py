#include <math.h>
#include <iostream>
using namespace std;

void print() {
	int i;
	for (i = 100; i < 1000; i++) 
		if (i % 10 == i / 100) 
			cout << "i = " << i << "£¬" << sqrt((double)i) << endl;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T, t;
	int a, b;
	int cnt;
	//print();
	cin >> T;
	for (t = 1; t < T + 1; t++) {
		cin >> a >> b;
		cnt = 0;
		cout << "Case #" << t << ": ";
		if (a <= 1 && b >= 1) cnt++;
		if (a <= 4 && b >= 4) cnt++;
		if (a <= 9 && b >= 9) cnt++;
		if (a <= 121 && b >= 121) cnt++;
		if (a <= 484 && b >= 484) cnt++;
		cout << cnt << endl;
	}
	return 0;
}