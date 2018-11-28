#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <tr1/unordered_map>
#include <windows.h>

using namespace std;
using namespace tr1;

#define ft first
#define sd second

typedef long long LL;
typedef unsigned int UI;

const int MAXN = 511111;
const int MOD = 1e9 + 7;
const double eps = 1e-6;
const LL MAXL = (LL)(0x7fffffffffffffff);
const int MAXI = 0x7fffffff;

double r[111], c[111];

int main(){

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	

	int T;
	cin >> T;
	for(int cases = 1; cases <= T; cases++){
		int n;
		cin >> n;
		double  v, x;
		cin >> v>> x;
		for(int i = 0; i < n; i++){
			cin >> r[i] >> c[i];
		}
		bool yy = true;
		double t = 0, t1 = 0 , t2 = 0;
		if(n == 2){
			if(c[0] == c[1]){
				r[0] += r[1];
				n = 1;
			}
			else if(c[0] == x){
				n = 1;
			}
			else if(c[1] == x){
				r[0] = r[1];
				c[0] = c[1];
				n = 1;
			}
		}
		if(n == 1){
			if(x != c[0]) yy = false;
			t = v / r[0];
		}
		else{
			double a = c[0] - c[1], b = x - c[1], q = c[0] - x;
			t1 = v * b / r[0] / a, t2 = v * q / r[1] / a;
			if(t1 < 0 || t2 < 0) yy = false;
			t = max(t1, t2);
		}
		printf("Case #%d: ", cases);
		if(yy) printf("%.7lf\n", t);
		else puts("IMPOSSIBLE");
	}
}
