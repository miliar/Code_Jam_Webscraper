#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> point;
#define X first
#define Y second

bool possible[17];

void read() {
	int a, p;
	cin >> a;
	--a;
	forn(i, 4)
		forn(j, 4)
			cin >> p, possible[p-1] = i == a;

	cin >> a;
	--a;
	forn(i, 4)
		forn(j, 4)
			cin >> p, possible[p-1] &= i == a;
			
	int lst = 0, cnt = 0;
	forn(i, 16)
		if (possible[i]) {
			cnt++;
			lst = i+1;
		}
		
	if (cnt == 1)
		cout << lst;
		
	if (cnt == 0)
		cout << "Volunteer cheated!";
		
	if (cnt > 1)
		cout << "Bad magician!";
}

void solve() {
	
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(i, t) {
		cout << "Case #" << i+1 << ": ";
				read();
		cout << "\n";
	}
	
	return 0;
}