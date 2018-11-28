#include <bits/stdc++.h>
using namespace std;
string to_s(char c){
	string a= "A" ;a[0]=c;
	return a;
}
main(){
	ios::sync_with_stdio(false) ;
	int t;
	cin >> t ;
	int j=1;
	while(t--){
		string s ;
		cin >> s ;
		string ans = "" ;
		ans += to_s(s[0]) ;
		for(int i=1;i<s.size();i++){
			if(ans[0]<=s[i]){
				ans = to_s(s[i])+ans ;
			}
			else ans+= to_s(s[i]) ;
		}
		cout << "CASE #"<<j<<": "<<ans<<endl;j++;
	}
}
