#include <iostream>
#include <string>
using namespace std;
// main function
int main(){
	
	int t;
	cin >> t;
	
	for(int l = 1; l <= t; l++){
		string ans;
		int x, r, c;
		
		cin >> x >> r >> c;
		
		int a = r*c;
		
		if( a%x == 0 && ((x <= r && c >= x-1)||(x <= c && r >= x-1)))
			ans = "GABRIEL";
		else
			ans = "RICHARD";
		
		cout << "Case #" << l << ": " << ans << endl; 
	}
	return 0;
}
