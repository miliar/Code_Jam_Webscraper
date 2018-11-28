#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <set>
#include <vector>


using namespace std;



int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int j = 0; j < t; j++) {
		string s;
		cin >> s;
		cout << "Case #" << j + 1 << ":" << " ";
		int n = 0;
		for (int i = 0; i < s.size() - 1; i++) {
			if (s[i] != s[i + 1]) {
				n++;
			}
		}
		if (s[s.size() - 1] == '-') {
			n++;
		}
		cout << n << endl;
	}

	//rm a.out; g++ A.cpp; ./a.out
}