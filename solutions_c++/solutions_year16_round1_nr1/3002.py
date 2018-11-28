#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<string>
#include<string.h>
#include<cmath>
#include<map>
#include<fstream>
using namespace std;

int main() {
	ifstream in("A-large (1).in");
	ofstream out("output.txt");
	char arr[10000];
	int t;
	in >> t;
	for (int z = 1; z <= t; ++z) {
		string s;
		in >> s;
		int l = 5000, r = 5000;
		arr[l] = s[0];
		for (int i = 1; i < s.size(); ++i) {
			if (arr[l] <= s[i]) {
				arr[l - 1] = s[i];
				l--;
			}
			else {
				arr[r + 1] = s[i];
				r++;
			}
		}
		out << "Case #" << z << ": ";
		for (int i = l; i <= r; ++i) {
			out << (char)arr[i];
		}
		out << endl;
	}
	return 0;
}