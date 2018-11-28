#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>

#define ull unsigned long long
#define ll long long

using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int x = 1; x <=t; x++) {
		int n;
		char in;
		int cur = 0;
		int re = 0;
		cin >> n;
		for (int i = 0; i<=n; i++) {
			cin >> in;
			in -= '0';
			if ( i > cur) {
				re += i - cur;
				cur += in + i - cur;
			}
			else cur += in;
		}
		cout << "Case #" <<x << ": "<< re << endl;
	}
	return 0;
}