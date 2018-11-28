#include<bits/stdc++.h>
using namespace std;
int main() {
	int tc,cnt=0;
	cin >> tc;
	while(tc--) {
		int w,ans=0,sum=0;
		cin >> w;
		string s;
		cin >> s;
		for(int i=0;i<=w;i++) {
			if(sum<i) {
				ans+=(i-sum);
				sum=i;
			}
			sum+=(s[i]-'0');
			//cout << sum << " " << ans << endl;
		}
		cout << "Case #"<< ++cnt << ": "<< ans << endl;
	}
	return 0;
}
