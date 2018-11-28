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

vector<int> result;
vector<int> winner;
int c[3];
int from;
int to;

void mock(int n) {
	result = vector<int>(to, 9);
	winner = vector<int>(to, 9);
	result[1] = 0;
	winner[1] = 0;
	for (int i = 2; i < to; i += 2) {
		int pre = result[i / 2];
		result[i] = pre;
		winner[i] = pre;
		result[i + 1] = (pre + 1) % 3;
		winner[i + 1] = pre;
	}
	c[0] = c[1] = c[2] = 0;
	for (int i = from; i < to; i++) {
		c[result[i]]++;
	}
}

void refine(string& s, int from, int to) {
	if (from + 1 == to)
		return ;
	int m = (from + to) / 2;
	refine(s, from, m);
	refine(s, m, to);

	bool yes = false;
	for (int i = 0; i < m - from; i++) {
		if (s[from + i] > s[m + i]) {
			yes = true;
			break;
		}
	}

	if (yes) {
		for (int i = 0; i < m - from; i++) {
			swap(s[from + i], s[m + i]);
		}
	}
}


int main() {
    ios::sync_with_stdio(false);

    int nc;
    cin >> nc;
    for (int t  = 1; t <= nc; t++) {
    	printf("Case #%d: ", t);
	    int n, p, r, s;
	    cin >> n >> r >> p >> s;
	    SHOW(p, r, s)

		from = 1 << n;
    	to = from + from;
    	SHOW(n, from, to)
	    mock(n);

    	for (int i = 1; i < to; i++) {
    		// cout << result[i];
    	}
    	// cout << endl;
	    
    	map<int, char> ok;
	    if (c[0] == p && c[1] == r && c[2] == s) {
	    	ok[0] = 'P';
	    	ok[1] = 'R';
	    	ok[2] = 'S';
	    }
	    else if (c[0] == p && c[1] == s && c[2] == r) {
			ok[0] = 'P';
	    	ok[1] = 'S';
	    	ok[2] = 'R';
	    }
	    else if (c[0] == r && c[1] == p && c[2] == s) {
			ok[0] = 'R';
	    	ok[1] = 'P';
	    	ok[2] = 'S';
	    }
	    else if (c[0] == r && c[1] == s && c[2] == p) {
			ok[0] = 'R';
	    	ok[1] = 'S';
	    	ok[2] = 'P';
	    }
	    else if (c[0] == s && c[1] == p && c[2] == r) {
			ok[0] = 'S';
	    	ok[1] = 'P';
	    	ok[2] = 'R';
	    }
	    else if (c[0] == s && c[1] == r && c[2] == p) {
			ok[0] = 'S';
	    	ok[1] = 'R';
	    	ok[2] = 'P';
	    }
	    else {
	    	cout << "IMPOSSIBLE" << endl;
	    }

	    if (ok.size() == 3) {
		    SHOW(ok[0], ok[1], ok[2])
	
	    	string ans = "";
	    	for (int i = from; i < to; i++) {
	    		ans += ok[result[i]];
	    	}
	    	refine(ans, 0, ans.length());
	    	cout << ans << endl;
	    }
    }
}

