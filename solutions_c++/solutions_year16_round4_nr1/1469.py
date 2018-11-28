#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

char wins(char x, char y) {
	if (x == 'P')
		return (y == 'R' ? x : y);
	if (x == 'R')
		return (y == 'S' ? x : y);
	return (y == 'P' ? x : y);
}

bool isterm(string a) {
	int n;
	while ((n = a.size()) > 1) {
		string b;
		for (int i = 0; i < n; i += 2) {
			if (a[i] == a[i+1])
				return false;
			b.push_back(wins(a[i], a[i+1]));
		}
		swap(a, b);
	}
	return true;
}

string solve(int N, int R, int P, int S) {
	string a = string(P, 'P') + string(R, 'R') + string(S, 'S');
	do {
		if (isterm(a))
			return a;
	} while (next_permutation(a.begin(), a.end()));
	return "IMPOSSIBLE";
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		string ans = solve(N, R, P, S);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}
