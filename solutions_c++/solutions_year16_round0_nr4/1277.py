#include <bits/stdc++.h>
using namespace std;
int t, k, c, s;
int main(){
	ios :: sync_with_stdio(false);
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);
	cin >> t;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ":";
		cin >> k >> c >> s;
		for(int i = 1; i <= k; i++) cout << " " << i;
		cout << '\n';
	}
}