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


void sol() {
	string s;
	cin >> s;

	string ans;
	ans += s[0];
	for (int i = 1; i < s.length(); i++) {
		char l = ans[0];
		char r = ans[ans.length() - 1];
		char cur = s[i];
		if (cur >= l) {
			ans = cur + ans;
		} else {
			ans = ans + cur;
		}
	}

	cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);

    int nc;
    scanf("%d", &nc);
    for (int i = 1; i <= nc; i++) {
    	printf("Case #%d: ", i);
    	sol();
    }
}





