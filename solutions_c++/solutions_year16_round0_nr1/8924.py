#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;
typedef long long int LLI;

LLI f(LLI a) {
	if (a == 0) return 0;
	set<int> digits;
	LLI b = 0;
	int count = 0;
	while (digits.size() < 10 && count < 100000000) {
		count++;
		b += a;
		LLI c = b;
		while (c > 0) {
			digits.insert(c % 10);
			c /= 10;
		}
	}
	if(digits.size() == 10) return b;
	else return 0;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, N;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		LLI result = f(N);
		cout << "Case #" << (i + 1) << ": ";
		if(result != 0) cout << result << endl;
		else cout << "INSOMNIA" << endl;
	}
	return 0;
}