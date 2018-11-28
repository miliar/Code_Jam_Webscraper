#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		int N; cin >> N;
		int a[N];
		for (int i = 0; i < N; ++i) {
			cin >> a[i];
		}
		
		int first = 0, second = 0, diff = 0;
		for (int i = 0; i < N-1; ++i) {
			if (a[i]-a[i+1] > 0) {
				first += a[i]-a[i+1];
			}
			if (a[i]-a[i+1] > diff) {
				diff = a[i]-a[i+1];
			}
		}
		for (int i = 0; i < N-1; ++i) {
			second += min(diff, a[i]);
		}
		cout << first << " " << second << endl;
	}
	
	return 0;
}