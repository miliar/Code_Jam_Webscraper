#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <memory.h>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << t << ": ";
		for (int i = 1; i <= s; i++) {
			cout << i << " ";
		}
		cout << endl;
	}


	//system("pause");
	return 0;
}