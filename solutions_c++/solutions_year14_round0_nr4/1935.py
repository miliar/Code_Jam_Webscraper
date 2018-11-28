#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int n;


vector<pair<double, int> > a;

void Load()
{
 	cin >> n;
 	double t;
 	a.clear();
 	int i;
 	for (i = 0; i < n; i++) {
 		cin >> t;
 		a.push_back(make_pair(t, 1));
 	}
 	for (i = 0; i < n; i++) {
 		cin >> t;
 		a.push_back(make_pair(t, -1));
 	}
 	sort(a.begin(), a.end());
 		
}

void Solve()
{
	int good = 0, bad = 0;
	int i;
	int cur = 0;
	for (i = 2*n-1; i >= 0; i--) {
		cur += a[i].second;
		if (cur > bad) bad = cur;
	}
	for (i = 0; i < 2*n; i++) {
		if (a[i].second == -1) cur++;
		else if (cur > 0) {
			cur--;
			good++;
		}
	}
	cout << good << ' ' << bad << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
