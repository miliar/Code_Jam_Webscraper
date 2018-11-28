#include <iostream>
#include <cstdio>
#include <cstring> 
using namespace std;
  

int main () {

	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int t, i, z, s_max, ctr, extra;
	string str;
	cin >> t;
	z = 1;
	while(t--) {
		cin >> s_max;
		cin >> str;
		ctr = extra = 0;	
		ctr += (str[0]-'0');
		for(i=1 ; i<= s_max ; i++) {
			if (ctr >= i) {
				ctr += str[i]-'0';
			}
			else {
				extra += 1;
				ctr += 1;
				ctr += str[i]-'0';
			}
		}
		cout << "Case #" << z++ << ": " << extra << "\n";
	}
	return 0;
}