#include<iostream>

using namespace std;

int main() {
	int T;
	int sMax;
	string sI;
	int sum = 0, ans = 0;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		sum = ans = 0;

		cin >> sMax;
		cin >> sI;

		for (int j = 0; j <= sMax; ++j) {
			sum += (sI[j]-'0');
			if (sum < (j+1)) {
				ans++;
				sum++;
			}
		}

		cout << "Case #" << (i+1) << ": "<< ans << endl;

	}


}
