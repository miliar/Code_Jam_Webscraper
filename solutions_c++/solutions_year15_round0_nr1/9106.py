#include<map>
#include<deque>
#include<queue>
#include<stack>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<set>
#include<list>
#include<climits>
#include<bitset>
#include<iterator>
#include<string.h>
#include<time.h>
#include<stdio.h>
#include<numeric> // accumulate
using namespace std;
#define print(A)    cout << #A << " = " << A << endl;
#define printt(A,B) cout << #A << " = " << A << " , " << #B << " = " << B << endl;
#define _c          cout << "--------" << endl;
#define all(v)      v.begin(), v.end()
#define rall(v)     v.rbegin(), v.rend()
#define clr(A,B)    memset(A,B,sizeof A);
#define sz(x)       (int)x.size()
#define mp(A, B)    make_pair(A, B)
typedef long long ll;
typedef long long unsigned llu;
//int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
//int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
//const double pi = 2 * acos(0.0);
//const int oo = (int) 2e9;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("bb.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	int h = 1;
	while (t--) {
		string s;
		cin >> s >> s;
		int ans = 0, cnt = 0;
		for (int i = 0; i < sz(s) ; ++i) {
			if (s[i] == '0')
				continue;
			if (i > cnt) {
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += s[i] - '0';
		}
		cout << "Case #" << h++ << ": " << ans << endl;
	}

	return 0;
}
