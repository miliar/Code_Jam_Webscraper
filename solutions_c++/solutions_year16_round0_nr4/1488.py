#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <unordered_map>


using namespace std;


int main() {
	//freopen("output.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << ii + 1 << ": ";
		for (int i = 0; i < s; i++) {
			cout << i + 1 << ' ';
		}
		cout << endl;
	}
    return 0;
}
