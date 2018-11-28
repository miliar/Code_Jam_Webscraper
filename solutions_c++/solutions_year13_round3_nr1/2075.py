#include <iostream>
#include <algorithm>

using namespace std;

string str;

int strcheck(int c, int e, int n){
	int cnt = 0;
	int max = 0;
	for(int i = c;i <= e; i++){
		if(str[i] != 'a' && str[i] != 'i' && str[i] != 'u' && str[i] != 'e'     && str[i] != 'o'){
			cnt++;
		}
		else{
			if(cnt > max){
				max = cnt;
			}
			cnt = 0;
		}
	}
	/*	else{
			cout << "cnt" << cnt << endl;
			if(cnt >= n){
				max++;
			}
				cnt = 0;
		}
*/
		if(cnt >= n){
			max = cnt;
		}
	
	if(max >= n){
		return 1;
	}
	return 0;
}

int main(){
	
	int t;
	cin >> t;
	for(int k = 1; k <= t; k++){
		int n;

		cin >> str >> n;
		
		int cnt;
		int ans = 0;
		for(int i = 0; i < str.length() - n + 1; i++){
			for(int j = i + n - 1; j < str.length(); j++){
				ans+= strcheck(i, j, n);
			}
		}
		
		cout << "Case #" << k <<": " << ans << endl;
	}
	return 0;
	
}
