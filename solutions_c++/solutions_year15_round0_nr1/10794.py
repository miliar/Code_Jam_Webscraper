#include <iostream>
#include <iomanip>
#include <vector>
#include <map>

using namespace std;

int main() {
	int cn;
	cin >> cn;
	for (int i = 0; i < cn; i++) {
		int s = 0, count = 0, needed = 0;
		char *p;
		cin >> s;
		p = new char[s + 2];
		cin >> p;
		for (int j = 0; j <=s; j++) {
			if (j > count && p[j] != '0') 
			{
				needed += j - count;
				count += needed;
			}
			count += (p[j] - '0');
		}
		cout << "Case #" << (i + 1) << ": " << needed << endl;
		delete []p;
	}
	return 0;
}
