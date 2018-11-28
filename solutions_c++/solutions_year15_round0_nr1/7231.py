#include <iostream>
#include <string>

using namespace std;

int main(){
	int t;
	cin >> t;
	
	for(int i=0; i<t; i++){
		int n;
		string s;
		cin >> n >> s;
		
		int ans = 0, sum=0;
		for(int j=0; j<s.length(); j++) {

			//cerr << "stand:" << sum << endl;
			//cerr << "j:" << j << endl;
			if(sum < j) {
				ans += j-sum;
				sum += j-sum;
			}
			sum += s[j] - '0';
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}	
	
	return 0;
}