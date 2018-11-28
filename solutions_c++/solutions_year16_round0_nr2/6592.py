#include <bits/stdc++.h>
#define mp make_pair
#define vi vector<int>
#define pi pair<int,int>
#define vii vector<pi>
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/shiva/Learning/1.txt", "r", stdin);
	freopen("/home/shiva/Learning/2.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false); cin.tie(0);
	int t, n, x = 1;
	bool flag;
	string s;
	cin >> t;
	while (t--) {
		cin >> s;
		n = 0; flag = false;
		int len = int(s.size());
		for (int i = len - 1; i >= 0;) {
			if (s[i] == '+' && (n % 2 == 0)) {i--; continue;}
			else {
				flag = false;
				while ((i >= 0) && (((s[i] == '+') && (n % 2 != 0)) || ((s[i] == '-') && (n % 2 == 0)))) {
					i--;
					flag = true;

				}
				if (flag) n++;
			}
		}
		cout << "Case #" << x << ": " << n << '\n'; x++;
	}


}