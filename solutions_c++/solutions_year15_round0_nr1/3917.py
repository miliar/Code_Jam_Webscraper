#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	int t, s, k = 1;
	string str;
	cin >> t;
	while( t-- ){
		cin >> s >> str;
		int ans = 0, emPe = 0;
		int qt = (str[0]-'0');
		emPe = qt;
		for( int i = 1; i < str.size(); i++ ){
			qt = (str[i]-'0');
			if( qt == 0 ) continue;
			if( emPe >= i ) emPe += qt;
			else{
				ans += i - emPe;
				emPe += (i - emPe)+qt;
			}
		}
		cout << "Case #" << k++ << ": " << ans << '\n';
	}
	return 0;
}