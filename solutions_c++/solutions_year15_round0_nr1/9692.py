#include <iostream>
using namespace std;

int main() {
	int t, cases = 0;
	cin >> t;
	
	while (t--){
		int a;
		string b;
		cin >> a >> b;
		
		int sum = b[0]-'0';
		int diff = 0;
		for (int i = 1; i < b.length(); i++){
			if (sum < i){
				diff += i-sum;
				sum = i;
			}
			sum += b[i]-'0';
		}
		
		cout << "Case #" << ++cases << ": " << diff << endl;
	}
	return 0;
}