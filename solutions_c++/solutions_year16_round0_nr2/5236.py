#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define ll long long
#define EPS 1e-7
using namespace std;
bool check(int a[]){
	for (int i = 0; i < 10; ++i){
		if (a[i] == 0)
			return false;
	}
	return true;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t, n,ans=0;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		string s1,s2;
		ans = 0;
		cin >> s1;
		s2 += s1[0];
		for (int i = 1; i < s1.length(); ++i){
			if (s1[i] != s2[s2.length() - 1])
				s2 += s1[i];
		}
		if (s2[0] == '-')
			ans += 1;
		for (int i = 1; i < s2.length();++i)
		if (s2[i] == '-')
			ans += 2;
		cout << "Case #" << k << ": " << ans << endl;
		
	}

	//system("pause");
}