#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define ll long long
#define EPS 1e-7
using namespace std;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	string s;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> s;
		string ans;
		ans += s[0];
		for (int i = 1; i < s.length(); ++i)
		{
			if (s[i] >= ans[0])
				ans = s[i] + ans;
			else ans += s[i];
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	
	
	
	
	
	//system("pause");
}