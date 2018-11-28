#include <iostream>
#include <string>
using namespace std;
int main(){
	int t, i = 0, b, j;
	char c[100], ch;
	cin >> t;
	for (i = 1; i <= t; i++) {
		j = 0;
		cin >> c;
		ch = c[0];
		b = strlen(c);
		for ( int r = 0; r < b; r++) {
			if (c[r] != ch) {
				j++;
				ch = c[r];
			}
		}
		if (c[b - 1] == '-') {
			j++;
		}
		cout << "Case #" << i << ": " << j << endl;
	}
	return 0;
}