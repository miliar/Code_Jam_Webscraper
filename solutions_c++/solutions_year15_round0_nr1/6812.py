#include<bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("codejam.txt","w",stdout);
	int T;
	cin >> T;
	for (int j = 1; j <= T; j++) {
		int n;
		string s;
		cin >> n >> s;
		int standing = s[0] - '0';
		int invited = 0;
		for (int i = 1; i < s.length(); i++) {
			if(standing<i&&s[i]!=0)
			{
				invited+=(i-standing);
				standing+=(i-standing);
			}
			standing+=(s[i]-'0');
		}
		printf("Case #%d: %d\n", j, invited);
	}
	return 0;
}
