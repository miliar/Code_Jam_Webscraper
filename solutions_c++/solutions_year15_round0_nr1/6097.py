#include <bits/stdc++.h>

using namespace std;

long long calc(string s) {
	long long ans = 0, sum = 0;
	
	
	for(int i = 0; i < s.size(); ++i) {
		if(sum < i) {
			ans += i - sum;
			sum = i;
		}
		sum += s[i] - '0';
	}
	
	return ans;
}

int main() {
	int t;
	cin >> t;
	
	for(int i = 0; i < t; ++i) {
		string s;
		int n;
		cin >> n >>s;
		
		cout << "Case #" << i + 1<< ": " << calc(s) << '\n';
	}
	
}