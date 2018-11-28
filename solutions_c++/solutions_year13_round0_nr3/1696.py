#include <iostream>
#include <cmath>
using namespace std;

char dataset[10000001];

int isPalin(long long test) {
	long long reverse = 0;
	long long forward = test;
	
	while (forward > 0) {
		reverse = reverse * 10 + (forward % 10);
		forward /= 10;
	}
	
	if (reverse == test)
		return 1;
	else
		return 0;
}

int main() {
	memset(dataset, -1, sizeof(dataset));

	int T = 0;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		long long possible = 0;
		long long a = 0;
		long long b = 0;
		
		cin >> a >> b;
		long long min = (long long) sqrt(a);
		long long max = (long long) sqrt(b);
		if (min * min < a)
			min++;
		
		for (long long test = min; test <= max; test++) {
			if (dataset[test] < 0)
				dataset[test] = isPalin(test);
			if (dataset[test]) {
				if (isPalin(test*test)) {
					possible++;
				}
			}
			
		}
		
		cout << "Case #" << t << ": " << possible << endl;
	}
	
	
	return 0;
}