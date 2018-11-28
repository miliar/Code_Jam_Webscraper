#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		long long n;
		cin >> n ;

		if ( n == 0 ) {
			cout<<"Case #"<<T<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int d[10] = {0,};
		for ( int i = 1 ; ; i++ ) {
			bool check = false;
			string s = std::to_string(n*i);
			sort(s.begin(), s.end());
			s.erase( unique(s.begin(), s.end()), s.end());

			for ( int j = 0 ; j < s.size(); j++) {
				d[ s[j] - '0' ] = 1;
			}
			
			int sum = 0;
			for(int i = 0 ; i < 10; i++) 
				sum += d[i];
			if (sum == 10) {
				cout<<"Case #"<<T<<": "<<n*i<<endl;
				break;
			}
		}
	}
	return 0 ;
}