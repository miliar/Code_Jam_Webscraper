#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:36777216")
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <climits>
#include <string>
#include <vector>
#include <cassert>
#include <ctime>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <hash_set>
#include <hash_map>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <bitset>

const long long MOD = 1000000000 + 7;
const long long MAXN = 100000 + 100;
const long long MAGIC = 123123123;

const double EPS = 1E-7;
#define TASK "taskname"
using namespace std;


struct cmp {
	bool operator()(const int & a, const int & b){
		return a > b;
	}
};



int main(){
	freopen("A-large (1).in", "r", stdin); freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int T = 1; T <= tc; ++T) {
		int mx;
		cin >> mx;
		string str;
		cin >> str;
		int res = 0;
		int cc = str[0] - '0';
		for (int i = 1; i < (int)str.size(); ++i) {
			res = max(res, i - cc);
			cc += str[i] - '0';
		}
		printf("Case #%d: %d\n", T, res);
	}

	return 0;
}