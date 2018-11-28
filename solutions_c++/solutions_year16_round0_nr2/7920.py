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
int t;
string str;

int main() {
	ios_base::sync_with_stdio(false);
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	//const clock_t beg = clock();

	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> str;
		bool ok = 0;
		int c = 0;
		while (!ok) {
			ok = 1;
			bool pl = 0;
			int mc = 0;
			for (int i = 0; i <= str.size(); i++) {
				if (i == str.size()) {
					if (pl && mc) {
						for (int e = 0; e < i; e++)
							str[e] = '-';
						c++;
					}
					else if (!pl && mc) {
						for (int e = 0; e < i; e++)
							str[e] = '+';
						c++;
					}
					break;
				}
				if (str[i] == '-') {
					mc++;
					ok = 0;
				}
				if (!pl && str[i] == '+' && mc) {
					for (int e = 0; e < i; e++)
						str[e] = '+';
					mc = 0;
					c++;
				}
				else if (pl && str[i] == '-') {
					for (int e = 0; e < i; e++)
						str[e] = '-';
					pl = 0;
					c++;
				}
				if (str[i] == '+')
					pl = 1;
			}
		}
		cout << "Case #" << tc << ": " << c << '\n';
	}

	//cout << double(clock() - beg) / CLOCKS_PER_SEC << '\n';
	return 0;
}