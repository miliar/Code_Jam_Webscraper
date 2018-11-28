#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
#define re return
#define LL long long
#define EPS 0.00000000001
#define MOD 1000000000
#define INF 2000000000
#define N 1008


LL n, a[N], c[N];

int main(){
#ifndef ONLINE_JUDGE
	ifstream cin("B-large.in");
	ofstream cout("A.out");
#endif
	
	int T;
	cin >> T;
	for (int t1 = 0; t1 < T; ++t1) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
		}
		sort(a, a + n);
		LL res = -1;
		if (a[n - 1] == 0)res = 0;
		else{
			for (int steps = 1; steps < N; ++steps) {
				LL k = 0;
				for (int i = 0; i < n; ++i) {
					c[i] = a[i];
				}
				for (int ifinish = n - 1; ifinish >= 0 && c[ifinish] > steps; --ifinish) {
					LL t = c[ifinish] / steps;
					c[ifinish] %= steps;
					if (!c[ifinish])t -= 1;
					k += t;
				}
				LL csteps = steps; for (int i = 0; i < n; ++i)csteps = max(csteps, c[i]);
				if (csteps + k < res || res == -1){
					res = csteps + k;
				}
			}
		}
		cout<<"Case #"<<t1+1<<": "<<res<<endl;
	}
	re 0;
}