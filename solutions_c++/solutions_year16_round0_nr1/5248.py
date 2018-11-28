#include <iostream>
#include <vector>
using namespace std;

int main() {

	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++) {
		
		int n;
		cin >> n;
		
		bool found = false;
		vector<bool> digits(10, false);
		long long curr = n;
		
		while(!found) {
			
			if (!curr) {
				break;
			}
			
			int t = curr;
			while(t) {
				digits[t%10] = true;
				t /= 10;
			}
			
			found = true;
			for(int i = 0; i < 10; i++)
				if (!digits[i]) {
					found = false;
					break;
				}
				
			curr += n;
		}
		
		if (found) {
			cout << "Case #" << t << ": " << curr - n << endl;
		} else {
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
	}
	
	return 0;
}