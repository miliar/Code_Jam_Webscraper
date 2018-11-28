#include <iostream>
using namespace std;
#include <cmath>

int s, a[1001], t;
char c;

int main() {
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #"<<i+1<<": ";
		
		cin >> s;
		
		for (int j = 0; j < s+1; j++) {
			cin >> c;
			if (c == ' ' || c == '\n') {
				j--;
				continue;
			}
			a[j] = c-'0';
		}
	/*	
		cout << s <<endl;
		for (int j = 0; j <= s; j++)
			cout << a[j]<< " ";
		cout << endl;*/
		
		int upnow = 0, minnec = 0;
		for (int j = 0; j <= s; j++) {
			minnec += max(0, j-upnow);
			upnow += a[j]+max(0, j-upnow);
		}
		cout << minnec << endl;
	}
	return 0;
}