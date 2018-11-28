#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

long long solve(long long n){
	if(n < 1) return -1;
	bool found[10] = {false};
	int count = 0;
	long long result = 0;

	while(true) {
		count++;
		long long x = count * n;
		result = x;
		while(x) {
			found[x % 10] = true;
			x /= 10;
		}

		for(int i = 0; i < 10; i++) {
			if(!found[i]) break;
			if(i == 9) return result;
		}

	}
}

int main() {
	int t;
	long long n;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		long long res = solve(n);
		if(res > 0)
			cout << "Case #" << (i + 1) << ": " << res << endl;
		else
			cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
	}

	return EXIT_SUCCESS;
}
