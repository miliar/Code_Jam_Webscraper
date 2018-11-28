#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <algorithm>
#include <iomanip>
#include <complex>
#include <valarray>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define rep(i,s,e) for (int i=(s);i<(e);++i)
#define pb push_back
#define mk make_pair
#define fst first
#define snd second
#define all(x) begin(x), end(x)
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;
double a[1000], b[1000];
bool btaken[1000];
int n;

int war() {
	memset(btaken, 0, 1000 * sizeof(bool));
	int points = 0;
	rep(i,0,n) {
		int bi = 0;
		rep(j,0,n)
			if (!btaken[j]) {
				bi = j;
				if (b[j] > a[i])
					break;
			}
		btaken[bi] = true;
		if (a[i] > b[bi])
			points++;
	}
	return points;
}

int deceitful_war() {
	int points = 0;
	int j = 0;
	rep(i,0,n) {
		if (a[i] > b[j]) {
			j++;
		}
	}
	return j;
}

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t; cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cin >> n;
		rep (i,0,n)
			cin >> a[i];
		rep (i,0,n)
			cin >> b[i];
		sort(a, a+n);
		sort(b, b+n);
		cout << "Case #" << ti << ": " << deceitful_war() << " " << war() << endl;
	}
}
