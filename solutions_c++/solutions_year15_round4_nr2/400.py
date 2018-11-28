#include <iostream>
#include <cstdio>
#include <ctime>
#include <cassert>
#include <cmath>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

#ifdef WIN32
	#define lld "%I64d"
#else
	#define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 3 * 1e6;
const ll Q = 1e9 + 7;

const db eps = 1e-10;



db r[3], c[3];

db solve1(db r0, db c0, db V, db C){
	if (abs(C - c0) < eps)
		return V / r0;
	return -1.;
}

db solve2(db r1, db c1, db r2, db c2, db V, db C){        
	db v1 = V * (C - c2) / (c1 - c2), v2 = V * (c1 - C) / (c1 - c2);
	if (v1 < 0 || v2 < 0)
		return -1.;
	return v1 / r1 + v2 / r2;	
}

db get(db ans, db t){
	if (abs(t + 1) < eps)
		return ans;

	if (abs(ans + 1) < eps)
		return t;
	ans = min(ans, t);
	return ans;
}
int main(){
	srand(time(NULL));
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int tq = 1; tq <= t; tq++){
		db V, C;
		int n;
		db ans = -1;
		cin >> n >> V >> C;
		for (int i = 0; i < n; i++)
			cin >> r[i] >> c[i];

		if (n > 2){
			cout << "fail\n";
			continue;
		}
		if (n == 1){
			ans = solve1(r[0], c[0], V, C);     	
		}
		else{

			r[2] = r[1] + r[0];
			c[2] = (r[1] * c[1] + r[0] * c[0]) / (r[1] + r[0]);


			for (int tqq = 0; tqq < 3; tqq++){
				ans = get(ans, solve1(r[tqq], c[tqq], V, C));
				int tq1 = (tqq + 1) % 3;
				int tq2 = (tqq + 2) % 3;
				ans = get(ans, solve2(r[tq1], c[tq1], r[tq2], c[tq2], V, C));
			}
		}
		cout << "Case #" << tq << ": ";
		if (ans < 0)
			cout << "IMPOSSIBLE\n";
		else
			printf("%.10f\n", ans);	
	}


	return 0;
}	