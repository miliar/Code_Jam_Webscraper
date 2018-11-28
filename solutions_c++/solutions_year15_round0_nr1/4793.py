#include <iostream>
#include <cstdlib>
using namespace std;

// char str[1001];

int main() {
	// your code goes here
	int t,t1 = 1;
	cin >> t;
	while(t--){
		long long int smax,scopy,i = 0;
		string shy;
		// long long int smax;
		cin >> smax >> shy;
		scopy = smax + 1;
		long long int stcount = 0,need = 0;
		while(scopy--){
			// cout << (shy[i]-48);
			if(i<=stcount){
				// cout << "inside "  << endl;
				stcount += (shy[i]-48);
			}
			else {
				// cout << "inside else" << endl;
				need += (i-stcount);
				stcount = stcount + (i-stcount) + (shy[i]-48);
			}
			i++;
		}
		cout << "Case #" << t1 << ": "  << need << endl;
		t1++;
		
	}
	return 0;
}