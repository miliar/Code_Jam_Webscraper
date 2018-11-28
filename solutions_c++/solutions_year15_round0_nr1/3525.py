#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <list>
#include <iterator>
#include <functional>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pnt;
typedef vector <int> vi;
#define FILE "bermutation"
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pss pair <string, string>
int main() {
#ifdef HOME
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(FILE ".in", "r", stdin);
//freopen(FILE ".out", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int it = 0; it < t; it++){
		int n;
		cin >> n;
		string s;
		cin >> s;
		int cnt = 0,
			ans = 0;
		for (int i = 0; i < (int)s.size(); i++){
			if (cnt >= i){
				cnt += s[i] - '0';
			} else {
				ans += i - cnt;
				cnt = i;
				cnt += s[i] - '0';
			}
		}
		if (cnt > 0)
			cout << "Case #" << it + 1 << ": "<< ans << "\n";
		else
			cout << "Case #" << it + 1 << ": "<< 1 << "\n";
	}
	return 0; 
}
