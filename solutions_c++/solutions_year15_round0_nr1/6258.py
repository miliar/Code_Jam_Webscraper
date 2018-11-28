#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outpl.out","w",stdout);
	int t,cnt=1;
	cin >> t;
	while(t--) {
		int c=0;
		int ans=0;
		int n;
		string s;
		cin >> n;
		cin >> s;
		int l = s.length();
		for (int i=0;i<l;i++) {
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
