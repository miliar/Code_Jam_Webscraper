#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#define endl '\n'

using namespace std;

#define lli long long int

set<int> intersect(set<int> & f, set<int> & s) {
	set<int> res;
	for(set<int>::iterator i = f.begin(); i != f.end(); ++i) 
		if (s.find(*i) != s.end()) 
			res.insert(*i);
	return res;
}

set<int> possible(int ans) {
	set<int> res;
	for(int i = 1; i <= 4; ++i) {
		for(int j = 1; j <= 4; ++j) {
			int t;
			cin >> t;
			if (i == ans) res.insert(t);
		}
	}
	return res;
}

int main() {
ios_base::sync_with_stdio(0);
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
		int ans; 
		cin >> ans;
		set<int> f = possible(ans);
		cin >> ans;
		set<int> s = possible(ans);
		set<int> res = intersect(f, s);
		if (res.size() == 1) {
			cout << (*res.begin());
		} else if (res.size() > 1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}
	return 0;
} 