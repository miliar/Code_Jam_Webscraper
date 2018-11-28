//============================================================================
// Name        : osmos.cpp
// Author      : swem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t = 0;

	cin >> t;
	for (int caseIdx = 1; caseIdx <= t; caseIdx++) {
		long long int a;
		int n;
		cin >> a >> n;
		vector<long long int> motes(n + 1);

		for (int i = 1; i <= n; i++) {
			cin >> motes[i];
		}
		sort(motes.begin() + 1, motes.end());

		vector<int> operations(n + 1);
		long long int sum = a;
		int answer = n;
		for (int i = 1; i <= n; i++) {
			operations[i] = operations[i - 1];
			//cout << "mote" << motes[i] << endl;
			if (sum <= motes[i]) {
				if (sum < 2) {
					operations[i] = n * 2;
				} else {
					while (sum <= motes[i]) {
						sum = sum * 2 - 1;
						operations[i]++;
					}
				}
			}
			sum += motes[i];

			answer = min(answer, operations[i] + n - i);

			//cout << i << "\t" << operations[i] << "\t" << answer << endl;
		}
		cout << "Case #" << caseIdx << ": " << answer << endl;
	}
	return 0;
}
