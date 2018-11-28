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
#define all(x) (x).begin(),(x).end()
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

set<int> read() {
	set<int> ret;
	int a1;
	cin >> a1;
	for (int y = 1; y <= 4; y++) {
		int x1, x2, x3, x4;
		cin >> x1 >> x2 >> x3 >> x4;
		if (y == a1)
			ret = {x1, x2, x3, x4};
	}
	return ret;
}

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		auto sols1 = read();
		auto sols2 = read();
		int out = 0, item;
		for (int s : sols2)
			if (sols1.count(s)) {
				out++; item = s;
			}

		cout << "Case #" << ti << ": ";
		if (out == 0)
			cout << "Volunteer cheated!\n";
		else if (out == 1)
			cout << item << "\n";
		else
			cout << "Bad magician!\n";
	}
}
