#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <string>
#include <queue>
using namespace std;
#define DEBUG

int main(){
#ifdef DEBUG
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	int  t = 0, T, n;
	double C, F, X, ans, old, sum;
	cin >> T;
	while (++t <= T){
		cin >> C >> F >> X; n = 0; ans = 0; old = 0xffff; sum = 0;
		while (true){
			if (n >= 1) sum += C / (2 + (n-1) * F);
			ans = sum + X / (2 + n * F);
			if (ans > old) { ans = old; break; }
			else { old = ans; ++n; }
		}

		cout << "Case #" << t << ": " << fixed << setprecision(6) << ans << endl;
	}

	return 0;
}
