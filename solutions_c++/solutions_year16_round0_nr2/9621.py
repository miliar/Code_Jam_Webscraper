#include <iostream>
#include <stdlib.h>
#include <cstring>
using namespace std;
int main() {
	int t;
	int i, j, k;
	string n;
	int flip;
	int current;
	int len;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		current = -1;
		flip = 0;
		cin >> n;
		len = n.size();
		while (len >= 0) {
			if (n[len] == '+') {
				if (current == 0) {
					flip++;
				}
				current = 1;	
			}
			if (n[len] == '-') {
				if (current != 0) {
					flip++;
				}
				current = 0;
			}
			len--;
		}
		cout << "Case #" << i << ": " << flip << endl;
	}
	return 0;
}


