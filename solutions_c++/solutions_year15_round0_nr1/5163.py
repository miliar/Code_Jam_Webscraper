#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int T, smax;
	char c;
	
	cin.sync_with_stdio(false);
	
	cin >> T;
	
	for(int TCASE = 0; TCASE < T; TCASE++) {
		
		cin >> smax;
		
		int result = 0, clap = 0;
		cin.get();
		
		for(int i=0;i<=smax;i++) {
			c = cin.get();
			
			result = max(result, -clap);
			
			clap += c-'1'; 
		}
		
		cout << "Case #" << TCASE + 1 << ": " << result << '\n';
	}
	
	
	return 0;
}
