#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outp1.txt","w",stdout);
	int test,cnt=1;
	cin >> test;
	while(test--) {
		int c=0;
		int ans=0;
		int k;
		string s;
		cin >> k;
		cin >> s;
		int lt = s.length();
		for (int i=0;i<lt;i++) {
			if(c>=i) {
				c+=s[i]-'0';
			}
			else {
				ans += (i-c);
				c=i;
				c+=s[i]-'0';
			}
		}
		printf("Case #%d: ",cnt++);
		cout << ans << endl;
	}
}
