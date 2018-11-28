#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>

#pragma comment(linker, "/STACK:133217728")

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);

    int T;
	cin >> T;
	int cnt = 0;
	for(int t=1; t<=T; t++) {
		int x, m, n;
		cin >> x >> n >> m;
		cout << "Case #" << t << ": ";

		if(x == 1) {
			cout << "GABRIEL" << endl;
			continue;
		}
		
		if(n * m % x) {
			cout << "RICHARD" << endl;
			continue;
		}

		if(x == 2) {
			if(n == 1 && m == 1) {
				cout << "RICHARD" << endl;
			}
			else
			{
				cout << "GABRIEL" << endl;
			}
			continue;
		}

		

		if(x == 4) {
			if(max(n, m) < 4) {
				cout << "RICHARD" << endl;
				continue;
			}

			if(min(n, m) < 3) {
				cout << "RICHARD" << endl;
				continue;
			}

			cout << "GABRIEL" << endl;
			continue;
		}
		
		if(min(n, m) < (x + 1) / 2) {
			cout << "RICHARD" << endl;
			continue;
		}

		cout << "GABRIEL" << endl;
		continue;
	}
    return 0;
}