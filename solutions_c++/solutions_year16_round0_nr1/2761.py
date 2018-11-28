#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

LL count(int n) {
	LL s = 0;
	bool f[10];
	memset(f, 0, sizeof(f));
	for (;;) {
		s += n;
		LL t = s;
		while (t) f[t % 10] = true, t /= 10;
		bool done = true;
		for (int i = 0; i < 10; ++i)
			if (!f[i]) {
				done = false;
				break;
			}
		if (done) break;
	}
	return s;
}

int main(){
	int T, n;
	cin >> T;
	for (int tn = 1; tn <= T; ++tn) {
		cout << "Case #" << tn << ": ";
		cin >> n;
		if (n == 0) cout << "INSOMNIA" << endl;
		else cout << count(n) << endl;
	}
}
