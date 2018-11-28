#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

#define oo 1e9
#define pi 3.1415926536
#define all(x) x.begin(),x.end()
#define sorta(x) sort(all(x))
#define sortam(x,comp) sort(all(x),comp)
#define sortd(x) sort(x.rbegin(),x.rend())
#define pb push_back
#define mp make_pair
#define sf(x) scanf("%d", &x);
#define sfll(x) scanf("%I64d", &x);
#define pr(x) printf("%d ", x);

typedef long long ll;
using namespace std;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		int x, r, c;
		cin >> x >> r >> c;
		if(r > c) swap(r, c);
		printf("Case #%d: ", tc);
		if(x == 1 || (x == 2 && (r % 2 == 0 || c % 2 == 0))) { cout << "GABRIEL\n"; continue; };
		if(x == 2 || r == 1 || x > c || (x == 3 && c != 3 && r!=3) || (x == 4 && r < 3)) { cout << "RICHARD\n"; continue; }
		cout << "GABRIEL\n";
	}

	return 0;
}
