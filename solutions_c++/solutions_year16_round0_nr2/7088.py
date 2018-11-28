/**
 * Created by zh0ng.
 */
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int cas=1;cas<=T;cas++){
		string s;
		cin >> s;
		int ans = 0;
		for(int i=s.length() - 1;i>=0;i--) {
			if(s[i] == '-') {
				ans++;
				for(int j=0;j<=i;j++) {
					s[j] = s[j] == '+' ? '-' : '+';
				}
			}
		}
		printf("Case #%d: %d\n",cas, ans);
    }

	return 0;
}
