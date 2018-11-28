#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}
#define PRINT(s, ...) {;}
#define PRINTLN(s, ...) {;}

// #undef HHHDEBUG
#ifdef HHHDEBUG
#include "template.h"
#endif

using namespace std;

template<typename T>
using Grid = vector<vector<T>>;

const double E = 1e-8;
const double PI = acos(-1);

#define DOWN '-'
#define UP '+'

int sol() {
	string s;
	cin >> s;

	int ans = 0;
	int i = 0;
	if (s[i] == DOWN) {
		ans++;
		while (s[i] == DOWN)
			i++;
	}
	int l = s.length();
	while (true) {
		while (i < l && s[i] == UP)
			i++;
		if (i == l)
			break;
		if (s[i] == DOWN) {
			ans++;
			ans++;
			while (i < l && s[i] == DOWN)
				i++;
		}
		if (i == l)
			break;
	}
	return ans;
}

int main() {
    ios::sync_with_stdio(false);

    int nc;
    scanf("%d", &nc);
    for (int i = 1; i <= nc; i++)
    	printf("Case #%d: %d\n", i, sol());
}






