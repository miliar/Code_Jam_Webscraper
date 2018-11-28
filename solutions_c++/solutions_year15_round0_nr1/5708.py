#include <iostream>
#include <string>
using namespace std;
// main function
int main(){
	
	int t;
	cin >> t;
	
	for(int l = 1; l <= t; l++){
		string s;
		int x, ans = 0;

		cin >> x >> s;
		
		int claps = 0;
		
		for(int i = 0; i <= x; i++){
			if( i <= claps || s[i] == '0'){
				claps += s[i] - '0';
			}else{
				ans += i - claps;
				claps = i;
				claps += s[i] - '0';
			}
		}
		
		cout << "Case #" << l << ": " << ans << endl; 
	}
	return 0;
}
