#include <iostream>

using namespace std;

int main() {
	int T; scanf("%d/n", &T);
//	cout << T << endl;
	for (int Ti = 0; Ti < T; Ti++) {
		long r, t, n; scanf("%ld %ld\n", &r, &t);
//		cout << r << " " << t << endl;
		for(long nn = 0; t >= 2*(r + 2*nn) + 1; nn++) {
			t = t - (2*(r + 2*nn) + 1);
			n = nn;
		}
//		cout << "Case #" << Ti+1 << ": " << n+1 << endl;
		printf("Case #%d: %ld\n", Ti+1, n+1);
	}
	return 0;
}
