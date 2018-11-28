#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

#define REP(i, a) for (int i = 0; i < (int)(a); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define CLEAR(x, val) memset(x, val, sizeof x)

int tc;
int n;
double naomi[1005], ken[1005];

int calc(double a[], double b[]) {
	int la = 0, ra = n - 1, lb = 0, rb = n - 1;
	int ans = 0;
	REP(i, n) {
		// can't win
		if (b[lb] > a[la]) {
			lb++; ra--;
		}
		else {
			lb++; la++;
			ans++;
		}
	}
	
	return ans;
}

bool cmp(double a, double b) {
	return a >= b;
}

int main () {
	cin >> tc;
	
	FOR(id, 1, tc) {
		cin >> n;
		REP(i, n)
			cin >> naomi[i];
		REP(i, n)
			cin >> ken[i];
			
		sort(naomi, naomi + n, cmp);
		sort(ken, ken + n, cmp);
		
		cout << "Case #"<< id << ": ";
		cout << " " << calc(naomi, ken) << " " << n - calc(ken, naomi) << endl;
	}
}
