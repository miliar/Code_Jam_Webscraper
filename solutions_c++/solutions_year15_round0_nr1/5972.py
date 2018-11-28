#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int count = 1; count <= t; count++) {
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int sum = 0;
		int result = 0;
		for(int i = 0; i <= smax; i++) {
			if(sum < i) {
				result += i-sum;
				sum += i-sum;
			}
			sum += s[i]-'0';
		}
		cout << "Case #" << count << ": " << result << endl;
	}
	return 0;
}

