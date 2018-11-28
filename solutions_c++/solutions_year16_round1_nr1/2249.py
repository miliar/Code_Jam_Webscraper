#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int n;

int t;

string s;
string ans;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A_output.txt", "w", stdout);
	cin >> t;
	int i,j;
	for(i = 1; i <= t; i ++) {
		cin >> s;
		ans = "";
		ans += s[0];
		for(j = 1; j < s.length(); j ++) {
			if(s[j] > ans[0]) {
				ans = s[j] + ans;
			} else if(s[j] < ans[0]){
				ans += s[j];
			} else {
				if(s[j] < ans[j - 1]) {
					ans += s[j];
				} else {
					ans = s[j] + ans;
				}
			}
		}
	
		cout << "Case #" << i << ": " << ans << endl;
	}

	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
