#include <iostream>

using namespace std;

unsigned int tc() {
	
	unsigned int ans = 0;
	unsigned int sum = 0;

	int smax;
	string s;

	cin >> smax;
	cin >> s;
	int n1;
	for( int i = 0; i < smax ; i++ ) {
		
		n1 = s[i] - '0';
		sum += n1;
		if(i+1 > smax)
			return ans;
		else
			if( i+1 > sum) {
				ans += (i+1 - sum);
				sum += (i+1 - sum);
			}
	}

	return ans;

}

int main() {

	int t;

	cin >> t;

	for( int i=1; i <= t ; i++ ) {

		cout << "Case #" << i << ": ";
		cout << tc() << "\n";
	
	}

	return 0;
}