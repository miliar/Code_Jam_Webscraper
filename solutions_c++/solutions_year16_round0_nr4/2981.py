#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
int main() {
	freopen("D-small.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);
	int t, k, c ,s;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cin >> k >> c >> s;
		cout << "Case #" << tt <<":";
		for (int i = 1; i<=s ; i++) {
			cout << " " << i;
		}
		cout << endl;
	}
	return 0;
}
