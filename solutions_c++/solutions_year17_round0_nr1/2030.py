#include<bits/stdc++.h>
using namespace std;




void solve(){
	string S;
	long long K;
	cin >> S >> K;
	long long ans = 0;

	for(int left = 0; left <= S.length() - K; left++){
		if(S[left] == '-'){
			ans++;
			//flip
			for(int i = 0; i < K; i++){
				if(S[left + i] == '-'){
					S[left + i]  = '+';
				}else{
					S[left + i]  = '-';
				}
			}
		}
	}
	bool ok = true;
	for(int i = 0; i < S.length(); i++){
		if(S[i] == '-'){
			ok = false;
		}
	}
	if(ok){
		cout << ans << endl;
	}else{
		cout << "IMPOSSIBLE" << endl;
	}
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

