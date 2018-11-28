//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 10000001

vector<int64> numbers;

string toString(int64 n) {
	string res = "";
	do {
		res += (n % 10) + '0';
		n /= 10;
	} while (n);
	return res;
}

bool isPalind(int64 n) {
	string a = toString(n);
	string b = a;
	reverse(all(b));
	return a == b;
}

void init() {
	numbers.pb(1);
	for (int i = 2; i < maxN; i++)
		if (isPalind(i) && isPalind(i * (int64)i)) {
			numbers.pb(i * (int64)i);
		}
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("C.inp", "r", stdin);
		freopen("C.out", "w", stdout);
	#endif
	init();
	int64 lo, hi;
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		cin >> lo >> hi;
		printf("Case #%d: %d\n", ++caseNo, upper_bound(all(numbers), hi) - lower_bound(all(numbers), lo));
	}
	return 0;
}
