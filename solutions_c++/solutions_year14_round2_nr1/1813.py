#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdlib>
#include <ctime>

using namespace std;

int sdistance(string &l, string &r) {
    int d = 0;
    
    vector<pair<char, int> > lw, rw;

    char prev = l[0];
    int count = 1;
    for (int i = 1; i < l.size(); ++i) {
	if (l[i] != prev) {
	    lw.push_back(make_pair(prev, count));
	    prev = l[i];
	    count = 1;
	}
	else {
	    count++;
	}
    }
    lw.push_back(make_pair(prev, count));

    prev = r[0];
    count = 1;
    for (int i = 1; i < r.size(); ++i) {
	if (r[i] != prev) {
	    rw.push_back(make_pair(prev, count));
	    prev = r[i];
	    count = 1;
	}
	else {
	    count++;
	}
    }
    rw.push_back(make_pair(prev, count));

    if (rw.size() != lw.size()) return -1;

    for (int i = 0; i < rw.size(); i++) {
	if (rw[i].first != lw[i].first) return -1;

	d += abs(rw[i].second - lw[i].second);
    }

    return d;
}

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
	int m;
	cin >> m;

	vector<string> s;

	while(m--) {
	    string input;
	    cin >> input;	
	    s.push_back(input);
	}

	int res = sdistance(s[0], s[1]);

	if (res == -1) {
	    cout << "Case #" << i << ": " << "Fegla Won" << endl;
	}
	else {
	    cout << "Case #" << i << ": " << res << endl;
	}
    }

    return 0;
}
