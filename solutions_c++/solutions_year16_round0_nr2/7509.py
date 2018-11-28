#include <vector>
#include <queue>
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
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define fi first
#define se second
#define mp make_pair
#define sz(x) ((int)(x).size())
#define re return
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define abs(x) ((x) < 0 ? -(x) : (x))
#define INF 2000000000
#define sqr(x) ((x) * (x))
#define all(x) x.begin(), x.end()
#define fname "a"
#define MOD 1000000007

typedef long long ll;

ll T, n, used[11], k, cnt = 1, res;
string s;

int main() {

	ios_base::sync_with_stdio(0);

	#ifndef ONLINE_JUDGE
		freopen("a.in", "r", stdin);
		freopen("a.txt", "w", stdout);
	#endif
	
	cin >> T;

	while(T--) {
		cin >> s;

		n = sz(s);
		res = 0;
		for(int i = n - 1; i >= 0; i--) {
			if(s[i] == '-') {
				for(int j = i; j >= 0; j--)
					s[j] = (s[j] == '+' ? '-' : '+');
				res++;
			}
		}
		printf("Case #%d: %d\n", cnt++, res);
	}
	return 0;
}







