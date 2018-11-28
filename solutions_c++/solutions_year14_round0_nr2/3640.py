#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <windows.h>
#include <string>
#include <cctype>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <initializer_list>
#include <exception>
#include <time.h>

typedef long long ll;

using namespace std;

#define ONLINE_JUDGE
int main(int argc, char **argv) {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << fixed;
		cout << "Case #" << i << ": ";
		long double c, f, x;
		cin >> c >> f >> x;
		if (c > x) {
			cout << x / 2.0 << endl;
			continue;
		}
		long double cur = 2.0, time = 0;
		while (true) {
			long double t1 = c / cur + x / (cur + f);
			long double t2 = x / cur;
			if (t2 <= t1) {
				cout << setprecision(7) << t2 + time << endl;
				break;
			}
			else {
				time += c / cur;
				cur += f;
			}
		}
	}

	//system("pause");
	return 0;
}
