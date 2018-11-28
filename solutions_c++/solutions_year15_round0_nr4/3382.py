//============================================================================
// Name        : .cpp
// Author      : Moaz
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <limits.h>

using namespace std;

#define all(v) v.begin(),v.end()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define clr(v,val) memset(v,val,sizeof(v))
#define  ll long long

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<bool> vb;

string alpha = "abcdefghijklmnopqrstuvwxyz";
string alphC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main() {
 freopen ("D-small-attempt2 (1).in","r",stdin);
 freopen ("output.txt","w",stdout);

	string res1 = "RICHARD";
	string res2 = "GABRIEL";

	int t, x, r, c;
	cin >> t;
	for (int i = 1; i <= t; i++) {

		cin >> x >> r >> c;
		if (x == 1)
			printf("Case #%d: %s\n", i, res2.c_str());
		else if (x == 2 && (r * c) % 2 == 0)
			printf("Case #%d: %s\n", i, res2.c_str());
		else if (x == 3 && (r * c) % 3 == 0 && !(r * c == 3)) {
			printf("Case #%d: %s\n", i, res2.c_str());
		} else if (x == 4 && (r * c) % 4 == 0 && !(r * c == 4 ||r * c == 8)) {
			printf("Case #%d: %s\n", i, res2.c_str());
		}

		else
		printf("Case #%d: %s\n", i, res1.c_str());
	}

	return 0;
}
