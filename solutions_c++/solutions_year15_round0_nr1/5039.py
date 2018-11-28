#include <bits/stdc++.h>


using namespace std;


int main()
{
	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	
	cin >> t;
	string s;
	int n;
	for ( int k = 1; k<= t; k++) {
		cin >> n;
		cin >> s;
		
		int ans = 0;
		int curr = s[0] - '0';
		for ( int i = 1; i <= n; i++) {
			if ( curr < i && s[i] > '0') {
				ans += i - curr;
				curr += i - curr;
		//		cout << i << " " <<  ans << " " << curr << endl;
			}
		//	cout << ans << endl;
			curr += (s[i] -'0');
		//	cout << curr << endl;
		}
		
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
	
}
