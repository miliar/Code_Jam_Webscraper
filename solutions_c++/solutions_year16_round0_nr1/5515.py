#include <iostream>

using namespace std;

int main (int argc, char * argv[]) {
	int T, t = 1;
	cin >> T;
	while(t <= T) {
		long N, n, cur;
		cin >> n;
		if(!n) {
			cout << "Case #" << t <<": INSOMNIA" << endl;
			t++;
			continue;
		}
		unsigned long base = ~((~0ul) << 10);
		unsigned long mask = 0;
		cur = 0;
		while(mask ^ base) {
			cur += n;
			N = cur;
			while(N) {
				mask |= (1 << (N % 10));
				N /= 10;
			}
		}
		cout << "Case #" << t <<": " << cur << endl;
		++t;
	}
	return 0;
}