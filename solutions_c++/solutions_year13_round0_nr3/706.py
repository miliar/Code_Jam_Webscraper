/*
ID: oooctav1
PROG: checker
LANG: C++
*/
#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define N 100005

bool is_pal(int64_t x) {
	int64_t y = 0, z = x;
	while (z) {
		y = y * 10 + (z%10);
		z /= 10;
	}
	return y == x;
}

int main() {
//	freopen ("checker.out","w",stdout);
//	freopen ("checker.in","r",stdin);
	ios_base::sync_with_stdio(false);

	/*
	int t;
	cin >> t;
	string s;
  getline(cin, s);
	for (int tt = 1; tt <= t; tt++) {
		string s;
		getline(cin, s);

		cout << "Case #" << tt << ": " << rez << endl; 
	}
		*/

	int64_t pals[1000];
	int nrpals = 0;

	int64_t nr = 0;
	int64_t mmax = 10000000;
	for (int64_t i = 1; i<= mmax; i++) {
		if (is_pal(i) && is_pal(i * i)) {
			pals[nrpals++] = (i*i);
		}
	}
	int t;
	cin >> t;
	string s;
  getline(cin, s);
	int64_t a,b;
	for (int tt = 1; tt <= t; tt++) {
		cin >> a >> b;
		int nr = 0;
		for (int i = 0; i < nrpals; i++)
			if (pals[i] >= a && pals[i] <= b) nr ++;
		cout << "Case #" << tt << ": " << nr << endl; 
	}

	return 0;
}
