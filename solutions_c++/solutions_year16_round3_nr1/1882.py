//============================================================================
// Name        : 1c-a.cpp
// Author      :
// Version     :
//============================================================================
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

using namespace std;

int main() {
	int T, N;
	int P[26];
	int sum;
	cin >> T;
	FOR(t, 1, T) {
		cin >> N;
		sum = 0;
		REP(i, N) {
			cin >> P[i];
			sum += P[i];
		}
		int count = 0;
		cout << "Case #" << t << ": ";
		while (count < sum) {
			int max = -1;
			int maxIndex = -1;
			REP (i, N) {
				if (P[i] > max) {
					max = P[i];
					maxIndex = i;
				}
			}
			if (count == 0 && (sum % 2 != 0)) {
				cout << (char)('A' + maxIndex) << " ";
				P[maxIndex]--;
				count++;
			} else {
				cout << (char)('A' + maxIndex);
				P[maxIndex]--;
				REP(i, N) {
					if (P[i] != 0 && i!= maxIndex) {
						cout << (char)('A' + i) << " ";
						P[i]--;
						break;
					}
				}
				count += 2;
			}
		}
		cout << endl;
	}

	return 0;
}
