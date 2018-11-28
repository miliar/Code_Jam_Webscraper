#include <bits/stdc++.h>

using namespace std;

int smax;
string s;

void input(){
	cin >> smax >> s;
}

void solve(){

	int num = s[0] - '0';
	int res = 0;

	for ( int i = 1 ; i <= smax ; i ++ ){
		int cur = s[i] - '0';
		if ( num < i && cur) res += (i-num) , num = i;
		num += cur;
	}

	cout << res << '\n';

}

int main(){

	freopen("A.inp" ,"r" ,stdin);
	freopen("A.out" ,"w", stdout);
	int T;
	cin >> T;

	for (int t = 1 ; t <= T ; t ++){
		cout << "Case #" << t << ": ";
		input();
		solve();
		
	}
}