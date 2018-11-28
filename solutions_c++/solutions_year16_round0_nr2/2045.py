#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solve(string coin) {
	int count = 0;
	while (coin.size() > 0) {
		int s = coin.size();
		while (s > 0 && coin[s - 1] == '+') s--;
		coin = coin.substr(0, s);
		if (coin.size() == 0) return count;
		if (coin[0] == '+') {
			int i = 0;
			while (coin[i] == '+') coin[i++] = '-';
		} else {
			for (int i = 0; i < coin.size(); i++) {
				if (coin[i] == '+') coin[i] = '-';
				else coin[i] = '+';
			}
		}
		count += 1;
	}
	return count;
}

int main(int argc, char const *argv[]) {
	int testcases;
	cin >> testcases;
	for (int i = 1; i <= testcases; i++) {
		string coins;
		cin >> coins;
		int good = true;
		int res = solve(coins);
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}