#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;

int a, b,q,z,v,x,r[2], c[2], pos, n, i;
double res, pr, v0, v1; 

int read() {
	scanf("%d.%d",&a, &b);
	//cout << a * 10000 + b << endl;
	return a * 10000 + b;
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
	scanf("%d",&n);
	v = read();
	x = read();
	for (i=0;i<n;i++) {
		r[i] = read();
		c[i] = read();
	}
	pos = 1;
	if (n == 1) {
		if (c[0] != x) {
			pos = 0;
		} else {
			res = v * 1.0 / r[0];
		}
	} else if (n == 2) {
		if (c[0] > c[1]) {
			swap(c[0], c[1]);
			swap(r[0], r[1]);
		}
		if (c[1] < x || c[0] > x) {
			pos = 0;
		} else if (c[0] == x && c[1] == x) {
			res = v * 1.0 / (r[0] + r[1]);
		} else if (c[0] == x) {
			res = v * 1.0 / r[0];
		} else if (c[1] == x) {
			res = v * 1.0 / r[1];
		} else {
			pr = (c[1] - x) * 1.0 / (c[1] - c[0]);
			//cout << pr << endl;
			v0 = v * pr;
			v1 = v - v0;
			res = max(v0 / r[0], v1 / r[1]);
		}
	}
	if (pos == 0) {
		printf("Case #%d: IMPOSSIBLE\n", q);
	} else {
		printf("Case #%d: %.9lf\n", q, res);
	}
}
return 0;
}

