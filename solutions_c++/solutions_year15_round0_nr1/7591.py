#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T, n;
	string s;
	cin >> T;
	for(int cas = 1;cas <= T;cas++){
		cin >> n >> s;
		int total = 0,ans = 0;
		for(int i = 0;i <= n;i++) {
			if (total < i) {
				ans += i - total;
				total = i;
			}
			total += s[i] - '0';
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
