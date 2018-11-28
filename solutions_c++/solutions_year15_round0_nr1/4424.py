/*
 * problem-A-small.cpp
 *
 *  Created on: Apr 11, 2015
 *  Author: Karim Mostafa
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <math.h> 
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ext/numeric>
#include <memory.h>
#include <valarray>
#include <limits>
using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("out.txt","w",stdout);

	int t;
	string str;
	int out = 0;
	int cur = 0;
	int tmp;
	cin >> t;

	for (int k = 1; k <= t; k++) {
		cin >> tmp;
		cin >> str;
		out = 0;
		cur = 0;
		for (int i = 0; i < (int) str.size(); i++) {
			if (i > cur) {
				out += (i - cur);
				cur = i;
			}

			cur += str[i] - '0';
		}

		cout << "Case #" << k << ": " << out << endl;
	}
	return 0;
}
