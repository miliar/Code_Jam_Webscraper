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

bool check(vector<int> &arr, int val){
	bool ok = true;
	int was = val;
	was += arr[0];
	for(int i = 1; i < sz(arr); ++i){
		if (arr[i] && was < i){
			ok = false;
			break;
		}
		was += arr[i];
	}
	return ok;
}

void solve(int cnt){
	int ans = 0;
	int n;
	cin >> n;
	string shy;
	cin >> shy;
	vector<int> arr(len(shy));
	forn(i, sz(arr)) arr[i] = shy[i] - '0';
	int l = -1, r = 1e+9;
	while(r - l > 1){
		int middle = (r + l) >> 1;
		bool ok = check(arr, middle);
		if (ok) r = middle;
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
