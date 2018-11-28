//#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<cmath>
#include<climits>
#include<list>
#include<utility>
#include<memory>
#include<cstddef>
#include<iterator>
#include<iomanip>
using namespace std;
typedef long long LL;
typedef long double LD;
const double pi = acos(-1.0);
///////////////////////////////


LL he(LL i) {
	LL lim = sqrt(i);
	for (LL t = 2; t <= lim; t++) {
		if (i%t == 0)return t;
	}
	return -1;
}


///////////////////////////////
int main(int argc, char**argv) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("outputc.out", "w", stdout);
	////////////////////////////

	int T;
	cin >> T;
	while (T--) {
		int ti = 1;
		cout << "Case #" << ti++ << ":" << endl;
		int n, j;
		cin >> n >> j;
		int cnt = 0;
		for (LL i = pow(10, n - 1) + 1; i <= 1.2*pow(10, n - 1); i++) {

			LL th = i;
			int a[100];
			int u = 1;
			for (; ; ) {
				int he = th % 10;
				a[u] = he;
				u++;
				th /= 10;
				if (th == 0) break;
			}
			u--;
			if (a[1] != 1)continue;
			if (a[u] != 1)continue;
			int war = 0;
			for (int p = 2; p <= u - 1; p++) {
				if (a[p] != 1 && a[p] != 0) {
					war = 1;
					break;
				}
			}
			if (war == 1) continue;
			queue<LL>Q;
			Q.push(i);
			int flag = 0;
			for (int p = 2; p <= 10; p++) {
				LL ans = 0;
				for (int k = 1; k <= u; k++) {
					ans += a[k] * pow(p, k - 1);
				}
				LL ou = he(ans);
				if (ou == -1) {
					flag = 1;
					break;
				}
				Q.push(ou);
			}
			if (flag == 1) {
				continue;
			}
			while (!Q.empty()) {
				LL ot = Q.front();
				Q.pop();
				cout << ot << " ";
			}
			cout << endl;
			cnt++;
			if (cnt == j) break;


		}



	}





	////////////////////////////
	//system("pause");
	return 0;
}

//END
