#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
int solve(){
	string s;
	cin >> s;
	s.push_back('+');
	int ans = 0;
	for(int i = 0; i < s.size()-1; ++i)
		if(s[i]!=s[i+1])
			++ans;
	return ans;
}
int main(){
	int n;
	cin >> n;
	for(int t = 1; t <= n; ++t){
		cout << "Case #" << t << ": ";
		cout << solve() << '\n';
	}
}

