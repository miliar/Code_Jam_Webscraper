#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int t;
string s;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large-out.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> s;
		int ans = 0;
		for (int j = 0; j < (int)s.length() - 1; j++){
			if (s[j] == '-' && s[j + 1] == '+'){
				ans++;
			} else if (s[j] == '+' && s[j + 1] == '-'){
				ans++;
			}
		}
		
		if (s[s.length() - 1] == '-'){
			ans++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
}
