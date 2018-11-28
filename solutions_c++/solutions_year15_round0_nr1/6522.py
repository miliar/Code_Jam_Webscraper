#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
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
#define _CRT_SECURE_NO_WARNINGS
#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

using namespace std;

int main() {
	string s;
	int cases=0;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	getline(cin, s);
	sscanf(s.c_str(), "%d", &cases);
	REP(k, cases) {
		getline(cin, s);
		stringstream st; st << s;
		int n; string sh;
		st >> n >> sh;
		int up = 0;
		int needed = 0;
		REP(i, sh.size()) {
			//printf("i = %d   up = %d   needed = %d\n", i, up, needed);
			if (up >= i) up += (sh[i] - '0');
			else {
				needed += (i - up);
				up += (i - up) + (sh[i]-'0');
				
			}
		}
		cout << "Case #" << (k + 1) << ": " << needed << endl;
	}
	return 0;
}
