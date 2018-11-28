#pragma warning (disable : 4996 4018)

#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <math.h>
#include <vector>
#include <bitset>
#include <climits>
#include <sstream>
#include <stdio.h>
#include <iomanip>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

const int MAX = 10000 + 9;
const double PI = 3.14159265358979323846;
unsigned long long t, n;
bool arr[10];

bool ok(unsigned long long nm) {
	stringstream ss;
	ss << nm;
	string str;
	ss >> str;
	for (int i = 0; i < str.size(); i++)
		arr[str[i] - '0'] = 1;
	for (int i = 0; i < 10; i++)
		if (!arr[i])
			return 0;
	return 1;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("A-large.in", "rt", stdin);
	//freopen("out.txt", "wt", stdout);
	//const clock_t beg = clock();

	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		memset(arr, 0, sizeof(arr));
		cin >> n;
		cout << "Case #" << tc << ": ";
		int i = 1;
		unsigned long long lst = -1;
		for (; ; i++) {
			if (lst == n*i) {
				cout << "INSOMNIA\n";
				break;
			}
			if (ok(n*i)) {
				cout << i*n << '\n';
				break;
			}
			lst = n*i;
		}
	}

	//cout << double(clock() - beg) / CLOCKS_PER_SEC << '\n';
	return 0;
}