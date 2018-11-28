#include <ctime>
#include <string>
#include <memory.h>
#include <iostream>

#define endl "\n"

using namespace std;

int main() { ios::sync_with_stdio(0); cin.tie(0);
	int T, X = 1;
	cin >> T;
	while(T--) {
		string s;
		cin >> s;
		int a[10];
		for(int i=0; i<10; i++) a[i] = 0;
		for(int i=0; i<s.size(); i++) {
			if(s[i] == 'Z') a[0]++;
			else if(s[i] == 'W') a[2]++;
			else if(s[i] == 'U') a[4]++;
			else if(s[i] == 'X') a[6]++;
			else if(s[i] == 'S') a[7]++;
			else if(s[i] == 'G') a[8]++;
			else if(s[i] == 'V') a[5]++;
			else if(s[i] == 'H') a[3]++;
			else if(s[i] == 'O') a[1]++;
		}
		a[1] = a[1] - a[0] - a[2] - a[4];
		a[3] = a[3] - a[8];
		a[7] = a[7] - a[6];
		a[5] = a[5] - a[7];
		a[9] = (s.size() - a[0]*4 - a[1]*3 - a[2]*3 - a[3]*5 - a[4]*4 - a[5]*4 - a[6]*3 - a[7]*5 - a[8]*5)/4;
		cout << "Case #" << X++ << ": ";
		for(int i=0; i<a[0]; i++) cout << "0";
		for(int i=0; i<a[1]; i++) cout << "1";
		for(int i=0; i<a[2]; i++) cout << "2";
		for(int i=0; i<a[3]; i++) cout << "3";
		for(int i=0; i<a[4]; i++) cout << "4";
		for(int i=0; i<a[5]; i++) cout << "5";
		for(int i=0; i<a[6]; i++) cout << "6";
		for(int i=0; i<a[7]; i++) cout << "7";
		for(int i=0; i<a[8]; i++) cout << "8";
		for(int i=0; i<a[9]; i++) cout << "9";
		cout << endl;/**/
	}
	return 0;
}