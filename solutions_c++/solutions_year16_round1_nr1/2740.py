#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
string s, ans;
int main() {
	int t, cas = 0;
	scanf("%d", &t);

	while(t--) {
		cin>>s;
		cas ++;
		char left,right;
		ans = "";
		int len = s.length();
		left = right = s[0];
		ans += s[0];
		for(int i = 1; i < len; i++) {
			if(s[i]>= left) {
				ans = s[i] + ans;
				left = s[i];
			} else {
				ans = ans + s[i];
				right = s[i];
			}
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
}