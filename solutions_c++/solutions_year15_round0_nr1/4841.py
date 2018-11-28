#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		int n;
		string s;
		cin >> n;
		cin >> s;
		int ans = 0, cur = 0;
		for(int i = 0; i <= n; ++i){
			if(i > cur){
				ans += (i - cur);
				cur = i;
			}
			cur += (s[i] - '0');
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
