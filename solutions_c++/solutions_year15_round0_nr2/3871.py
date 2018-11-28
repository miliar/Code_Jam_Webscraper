#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

int answer(map<int, int, greater<int> > counts) {
	int mx = counts.begin()->first;
	int mintime = mx;
	int mxcount = counts.begin()->second;
	counts.erase(counts.begin());
	for (int i = 1; i<=mx/2; i++) {
		counts[i] += mxcount;
		counts[mx-i] += mxcount;
		mintime = min(mintime, mxcount + answer(counts));
		counts[i] -= mxcount;
		counts[mx-i] -= mxcount;
	}
	return mintime;
}

int main()
{
	int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++){
		map<int, int, greater<int> > counts;
		int d;
		cin >> d;
		for (int i = 0; i < d; i++) {
			int temp;
			cin >> temp;
			counts[temp]++;
		}
		printf("Case #%d: %d\n", _t, answer(counts));
	}
    return 0;
}
