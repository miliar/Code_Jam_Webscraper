#include <iostream>
#include <string>
using namespace std;

int main() {
	
	int t;
	
	cin >> t;
	
	for(int ti = 1; ti <= t; ti++){
	    
	    string s;
	    cin >> s;
	    
	    string ans = "";
	    for(int i = 0; i < s.size(); i++){
	        if(ans == ""){
	            ans += s[i];
	            continue;
	        }
	        
	        if(ans[0] <= s[i]){
	            ans = s[i] + ans;
	        }else {
	            ans += s[i];
	        }
	    }

	    
	    cout << "Case #" << ti <<": " << ans << '\n';
	    
	}
	
	return 0;
}
