#include <bits/stdc++.h>
using namespace std;
int t, dp[105];
string s;
int main(){
	ios :: sync_with_stdio(false);
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);
	cin >> t;
	dp[0] = -1;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ": ";
		cin >> s; 
		s = "#" + s;
		dp[1] = (s[1] == '-');
		for(int i = 2; i < s.size(); i++){
			if(s[i] == '+') dp[i] = dp[i - 1];
			else{
				int j = i - 1;
				while(j >= 0 && s[j] == '-') j--;
				dp[i] = dp[j] + 2;
			}
		}
		cout << dp[(int)s.size() - 1] << '\n';
	}
}