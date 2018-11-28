#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		int x, r, c;
		cin >> x >> r >> c;

		if(r > c) {
			swap(r, c);
		}

		string s[2] = {"GABRIEL", "RICHARD"};
		int ans;

		if(x == 1) {
			ans = 0;
		} else if(x == 2) {
			if(r * c % 2 == 0) {
				ans = 0;
			} else {
				ans = 1;
			}
		} else if(x == 3) {
			if(r * c % 3 == 0) {
				if(r == 1) {
					ans = 1;
				} else {
					ans = 0;
				}
			} else {
				ans = 1;
			}
		} else {
			if(r * c % 4 == 0) {
				if(r == 1 || r == 2) {
					ans = 1;
				} else {
					ans = 0;
				}
			} else {
				ans = 1;
			}
		}

		cout << "Case #" << t << ": " << s[ans] << endl;
	}
}
