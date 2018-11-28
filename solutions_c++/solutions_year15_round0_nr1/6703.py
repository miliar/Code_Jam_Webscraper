#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	freopen("A-large.IN", "r", stdin);
	freopen("ouput.txt", "w", stdout);
	int t;
	cin >> t;
	int h = 0;
	while (t--) {
		int x;
		cin >> x;
		string z;
		cin >> z;
		int c = 0;
		int g = 0;
		for (int i = 0; i < z.size(); i++) {
			if (i > c) {
				while (c < i) {
					g++;
					c++;
				}
			}
			c += z[i] - 48;
			//cout << c << endl ;
		}
		cout << "Case #" << h + 1 << ": " << g << endl;
		h++;
	}
}
