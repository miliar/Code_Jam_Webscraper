#include <bits/stdc++.h>
using namespace std;
int main(){
	int T,s,curr,ans;
	string num;
	cin >> T;
	for(int j=1;j<=T;j++){
		cin >> s >> num;
		curr = num[0] - '0';
		ans = 0;
		for(int i=1;i<=s;i++){
			int val = max(i - curr,0);
			if(num[i]=='0') val = 0;
			ans += val;
			curr += val + num[i] - '0';
		}
		cout << "Case #" << j << ": " << ans << "\n"; 
	}
	return 0;
}