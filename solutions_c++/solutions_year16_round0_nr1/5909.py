#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 1; i<=t; i++) {
		int n;
		cin >> n;
		long long val = n;
		set<int> digits;
		digits.clear();
		cout << "Case #" << i << ": ";
		if (n==0)
			cout << "INSOMNIA" << endl;
		else {
			for(int j = 1; j < 200; j++) {
				val = n * j;
				long long temp = val;

				while (temp > 0) {
					digits.insert(temp%10);
					temp/=10;
					if (digits.size() >= 10){
						break;
					}
				}
				if(digits.size() >= 10)
					break;
			}

			if (digits.size() < 10)
				cout << "INSOMNIA" << endl;
			else 
				cout << val << endl;
		}
	}
	return 0;
}