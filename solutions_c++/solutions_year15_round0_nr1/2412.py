#include <iostream>

using namespace std;

int a[1001];

int main()
{
	int t, s;
	char c;
	cin >> t;
	for(int j = 1; j <= t; ++j) {
		cin >> s;
		for(int i = 0; i <= s; ++i) {
			cin >> c;
			a[i] = c - '0';
		}
		int cur = 0;
		int ans = 0;
		for(int i = 0; i <= s; ++i) {
			if(i > cur) {
				ans += (i - cur);
				cur = i;
			}
			cur += a[i];
		}
		cout << "Case #" << j << ": " << ans << endl;
	}
	return 0;
}
