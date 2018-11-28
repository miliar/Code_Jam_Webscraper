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
double c, f, x;

int main () {
	cin >> tc;
	
	FOR(id, 1, tc) {
		cin >> c >> f >> x;
		
		double rate = 2.00;
		double t = 0.00;
		double ans = (x / 2.00);
		double delta;
		
		FOR(i, 1, x) {
			delta = (c / rate);
			t += delta;
			rate += f;
			
			//printf("%7lf\n", t + (x / rate));
			
			ans = min(ans, t + (x / rate));
		}
		
		cout << "Case #"<< id << ": ";
		printf("%7lf\n", ans);
	}
}
