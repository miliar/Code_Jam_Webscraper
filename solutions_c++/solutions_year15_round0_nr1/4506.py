#include <fstream>
#include <iostream>
using namespace std;

int t, i, smax;
string s;

int main() {
	ifstream fi("a.in");
	ofstream fo("test.out");
	fi >> t;
	int c = 0;
	while(t--) {
		fi >> smax;
		fi >> s;
		int extra_friends = 0;
		int sum = 0;
		for (i = 0; i <= smax; i++) {
			int shyness = s[i] - '0';
			if (shyness > 0 and i > sum) {
				extra_friends += i - sum;
				sum += extra_friends;
			}
			sum += shyness;
		}
		fo << "Case #" << (++c) << ": "<< extra_friends << "\n";
	}
	return 0;
}