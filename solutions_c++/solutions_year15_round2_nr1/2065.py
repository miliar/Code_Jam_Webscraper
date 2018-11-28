#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


vector<int> dp(1000001, -1);


int reverse(int number) {
	string s = to_string(number);
	std::reverse(s.begin(), s.end());
	return atoi(s.c_str());
}

int calculate(int number) {
	if (dp[number] != -1) {
		return dp[number];
	} else {
		// we can either reverse or count one down:
		int r = reverse(number);
		if (r < number && (number % 10) != 0) {
			dp[number] = min(calculate(r + 1), calculate(number-1) + 1);
		} else {
			dp[number] = calculate(number-1) + 1;
		}	
	
	}

}

int main () {
	for (int i=0; i<=19; ++i) {
		dp[i] = i;
	}
	for (int i=0; i<=1000000; ++i) {
		calculate(i);
	}

	size_t numTestCases;
	cin >> numTestCases;
	for (size_t i=0; i<numTestCases; ++i) {
		int N;
		cin >> N;
		cout << "Case #" << (i+1) << ": " << calculate(N) << endl; 
	}
}
