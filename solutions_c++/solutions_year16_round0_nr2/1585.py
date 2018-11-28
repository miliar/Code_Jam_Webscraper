#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, ans=0, cas, i;
	string s;
	
	cin >> T;
	for(cas=1;cas<=T;cas++){
		cin >> s;
		ans = 0;
		i=1;
		if(s[0]=='-'){
			ans++;
		}
		for(;i<s.size();i++){
			if(s[i]=='-' and s[i-1]=='+') ans+=2;
		}
		cout << "Case #" << cas << ": " << ans << '\n';
	}
	return 0;
}
