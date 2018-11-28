#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
void solve(){
	string s;
	cin >> s;
	reverse(s.begin(), s.end());
	int inv = 0;
	int ans = 0;
	for(int i = 0; i < (int)s.size(); i++){
		if(inv ^ (s[i] == '-'))ans++, inv ^= 1;
		
	}
	cout << ans;
}
int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}
