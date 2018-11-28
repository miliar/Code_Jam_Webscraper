#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n;
		cin >> n;
		string s;
		cin >> s;
		
		int cur = s[0] - '0';
		int ans = 0;
		for(int i = 1; i <= n; i++){
			if(cur < i){
				ans += i - cur;
				cur += i-cur + (s[i] - '0');
			}else{
				cur += s[i]-'0';
			}
		}

		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}
