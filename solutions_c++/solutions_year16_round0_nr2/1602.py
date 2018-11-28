#include <iostream>
#include <string.h>

using namespace std;

int main(void) {
	string s;
	int n;
	cin >> n;
	int t;
	int l;
	for(int i=0; i<n; i++) {
		cin >> s;
		l=s.length();
		t=0;
		char pc=s[0];
		for(auto c : s) {
			if(c!=pc) t++;
			pc=c;
		} 				
		t+=(s[l-1]=='-')?1:0;
		cout << "Case #" << i+1 << ": " << t << endl;
		
	}
	return 0;
}
