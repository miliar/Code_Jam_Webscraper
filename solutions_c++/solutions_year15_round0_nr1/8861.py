#include <bits/stdc++.h>
using namespace std;
int f[10000], sum[10000];
int main() {
	int t;
	 freopen("A-large.in","r",stdin);
	 freopen("output.txt", "w", stdout);
	cin >> t;
	for (int c = 1; c <= t; c++) {
		for (int i = 0; i < 10000; i++)
			f[i] = 0, sum[i] = 0;
		int n, fr = 0;
		string s;
		cin >> n >> s;
		for (int i = 0; i < s.length(); i++)
			f[i] = s[i] - '0';
		sum[0] = f[0];
		for (int i = 1; i < s.length(); i++){
			if (f[i] && sum[i - 1] < i) {
				fr += (i - sum[i - 1]);
				sum[i-1]+=i-sum[i-1];
			}
			sum[i] = sum[i - 1] + f[i];
		}
		cout << "Case #" << c << ": " << fr << endl;
	}

	return 0;
}
