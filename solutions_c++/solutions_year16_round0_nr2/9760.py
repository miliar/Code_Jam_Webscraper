#include <iostream>
#include <string>
using namespace std;

int main() {
	int T, ans;
	string S;
	
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> S;
		
		if(S[S.length() - 1] == '-'){
			ans = 1;
		}
		else{
			ans = 0;
		}
		
		for(int j = S.length() -1; j > 0; j--){
			if(S[j] != S[j - 1]){
				ans++;
			}
		}
		
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	
	return 0;
}