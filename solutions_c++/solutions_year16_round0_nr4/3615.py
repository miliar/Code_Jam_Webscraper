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
	int k, c, s;
	for (int i = 0; i < t; i++) {
		cin >> k >> c >> s;
		cout << "Case #" << i + 1 << ":" << " ";
		for (int j = 0; j < k; j++) {
			cout << j + 1 << " ";
		}
		cout << endl;
	}
	cout << endl;
	//rm a.out; g++ A.cpp; ./a.out
}