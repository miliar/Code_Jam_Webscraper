#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int T;
	cin >> T;
	string s;
	int n;
	for (int t=1; t<=T; t++) {
		cin >> s;
		n = s.length();
		int ans = 0;
		for (int i=n-1; i>=0; i--) {
			if (s[i] == '+') continue;
			ans ++;
			for (int j=0; j<=i; j++) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}