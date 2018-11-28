#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas=1, i;
	char f, l;
	string s, ans;
	
	cin >> T;
	for(cas=1;cas<=T;cas++){
		cout << "Case #" << cas << ": ";
		cin >> s;
		f = s[0];
		l = f;
		ans = "";
		ans += f;
		for(i=1;i<s.size();i++){
			if(s[i]<f){
				ans += s[i];
				l = s[i];
			}
			else{
				ans = s[i]+ans;
				f = s[i];
			}
		}
		cout << ans << '\n';
	}
	return 0;
}
