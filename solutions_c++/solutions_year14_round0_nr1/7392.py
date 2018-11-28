//============================================================================
// Name        : cf.cpp
// Author      : HX
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>

using namespace std;
#define  N   211
#define  eps 1e-8
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 1000000007ll
#define  LL  long long


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for (int t=1; t<=T; t++) {
		map<int, int> a;
		vector<int> b;
		int k;
		cin >> k;
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				int x; cin >> x;
				if (i == k)
					a[x]++;
			}
		}
		cin >> k;
		int cao = 1;
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				int x; cin >> x;
				if (i == k)
					b.push_back(x);
			}
		}
		int cnt = 0;
		for (int i=0; i<4; i++)
			if (a[b[i]] != 0)
				cnt++, cao = b[i];
		cout << "Case #" << t << ": ";
		if (cnt == 1)
			cout << cao << endl;
		else if (cnt > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;

	}
	return 0;
}
