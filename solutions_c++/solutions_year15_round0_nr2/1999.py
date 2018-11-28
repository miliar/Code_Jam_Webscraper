#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef long long ll;
typedef double db;
typedef long double ldb;
typedef string str;

#define forn(i, n) for(int i = 0; i < n; ++i)
#define INF 1e+9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define X first
#define Y second
#define ms(x) memset(x, 0, sizeof(x))
#define ms1(x) memset(x, -1, sizeof(x))
#define sz(x) ( (int) x.size() )
#define len(x) ( (int) x.length() )
#define ALL(x) x.begin(), x.end()
#define pii pair<int, int>
#define pdd pair<double, double>

int cnt = 0;

bool check(vector<int> &arr, int t){
	for(int i=1; i < t; i++){
		priority_queue<int> q;
		forn(j, sz(arr)) q.push(arr[j]);
		int res = t - i;
		forn(j, i){
			int topp = q.top();
			q.pop();
			if (topp <= res) return true;
			topp -= res;
			q.push(topp);
			q.push(res);
		}
		if (q.top() <= res) return true;
	}
	return false;
}

void solve(int cnt){
	int ans = 0;
	int n;
	scanf("%d", &n);
	vector<int> arr(n);
	forn(i, n) {
		scanf("%d", &arr[i]);
		ans = max(arr[i], ans);
	}
	int l = 0, r = ans;
	while(r - l > 1){
		int middle = (r + l) >> 1;
		if (check(arr, middle)) r = middle;
		else l = middle;
	}
	ans = r;
	printf("Case #%d: %d\n", cnt, ans);
}

int main(){
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	while(t--) solve(++cnt);
#ifdef _DEBUG
	cout << fixed << setprecision(15) << clock() * 1. /  CLOCKS_PER_SEC;
#endif
	return 0;
}
