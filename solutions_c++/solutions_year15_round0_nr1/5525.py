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
#include <string>
#include <cstring>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-9
#define PI 3.14159265358979323846264338327950
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	ios::sync_with_stdio(false);
	int t, cs = 1;
	cin >> t;
	while (t--) {
		int n, res = 0, cur = 0;
		string s;
		cin >> n >> s;
		vi v(sz(s));
		FOR(i , 0 ,sz(s))
			v[i] = s[i] - '0';
		cur = v[0];
		FOR(i , 1 , n + 1)
		{
			if(v[i] && cur < i)
				res += (i - cur) , cur += (i - cur);
			cur += v[i];
		}
		cout << "Case #" << cs++ << ": " << res << endl;
	}
	return 0;
}
