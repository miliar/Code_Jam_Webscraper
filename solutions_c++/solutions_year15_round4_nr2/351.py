/*************************************************************************
    > File Name: B.cpp
    > Author: wmg_1001
    > Mail: wmg_1007@163.com 
    > Created Time: Sat 30 May 2015 10:39:10 PM CST
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <iomanip>
#include <algorithm>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

double x[2], v[2], X, V;

int main() {
	int T, case_T = 0;
	cin >> T;
	while (T--) {
		case_T++;
		cout << "Case #" << case_T << ": ";
		int n;
		cin >> n;
		cin >> V >> X;
		for (int i = 0; i < n; i++) cin >> v[i] >> x[i];
		if (n == 1) {
			if (X != x[0]) {
				cout << "IMPOSSIBLE" << endl;
			} else {
				printf("%.9lf\n", V / v[0]);
			}
		} else {
			if (X < min(x[0], x[1]) || X > max(x[0], x[1])) {
				cout << "IMPOSSIBLE" << endl;
			} else {
				if (X == x[0] && X == x[1]) {
					printf("%.9lf\n", V / max(v[0], v[1]));
				} else {
					if (X == x[0]) {
						printf("%.9lf\n", V / v[0]);
					} else {
						if (X == x[1]) printf("%.9lf\n", V / v[1]);
						else {
							double x00 = x[0] - X;
							double x11 = x[1] - X;
							double v00 = (V * x11) / (x11 - x00);
							double v11 = V - v00;
							printf("%.9lf\n", max(v00 / v[0], v11 / v[1]));
						}
					}
				}
			}
		}
	}
	return 0;
}



