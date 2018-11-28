#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <iomanip>
#include <cstdlib>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;

int main() {
	ios_base::sync_with_stdio(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;

	for(int test = 1; test <= T; test++) {
		int k;
		string s;
		cin >> k >> s;
		int ans = 0, sum = s[0] - '0';
		for(int i = 1; i <= k; i++) {
			if(sum < i) {
				ans += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}

		cout << "Case #" << to_string(test) << ": " << ans << '\n';
	}

	return 0;
}
