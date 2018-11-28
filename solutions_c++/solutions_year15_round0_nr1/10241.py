#include <cstdio>
#include <algorithm>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int T, S;
char tmp;

int main() {
    freopen("standingOvation.in", "r", stdin);
  	freopen("standingOvation.out", "w", stdout);
	cin >> T;

	for(int i = 0; i < T; i++) {
		cin >> S;
		long long sum = 0;
		long long localMax = 0;
		cin >> tmp;
		for(int j = 0; j < S; j++) {
			sum += tmp - '0';
			cin >> tmp;
			if(tmp != '0') {
				localMax += max((long long)0, j+1-sum);
				sum += localMax;
			}
		}
		cout << "Case #" << i+1 << ": " << localMax << "\n";
	}


	return 0;
}