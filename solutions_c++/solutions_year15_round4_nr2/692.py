#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int,int> PP;

/*
    freopen("input","r",stdin);
    freopen("output","w",stdout);
*/

int N;
vector<double> R;
vector<double> C;
double V,X,eps = 1E-9;
bool ok;

double solve() {
	ok = 0;
	if (N == 1) {
		if (abs(C[0] - X) < eps) {
			ok = 1;
			return V/R[0];
		}
		return 0.0;
	}
	if (C[0] > X + eps && C[1] > X + eps) {
		return 0.0;
	}
	if (C[0] < X - eps && C[1] < X - eps) {
		return 0.0;
	}
	if (abs(C[0] - X) < eps && abs(C[1] - X) < eps) {
		ok = 1;
		return V / (R[0] + R[1]);
	}
	if (abs(C[0] - X) < eps) {
		ok = 1;
		return V / R[0];
	}
	if (abs(C[1] - X) < eps) {
		ok = 1;
		return V / R[1];
	}
	double r1 = abs(C[0] - X);
	double r2 = abs(C[1] - X);
	double v1 = V * r2 / (r1 + r2);
	double v2 = V * r1 / (r1 + r2);
	ok = 1;
	return max(v1/R[0],v2/R[1]);
}

int main() {
	freopen("B-small-attempt0.in.txt","r",stdin);
    freopen("output","w",stdout);
    ios::sync_with_stdio(false);
    cout.precision(20);
    int T,z,i,j,k;
    cin >> T;
    for (z = 1;z <= T;z++) {
    	cin >> N;
    	R.clear();
    	R.resize(N);
    	C.clear();
    	C.resize(N);
    	cin >> V >> X;
    	for (i = 0;i < N;i++) {
    		cin >> R[i] >> C[i];
    	}
    	double res = solve();
    	if (ok == 0) {
    		cout << "Case #" << z << ": IMPOSSIBLE" << endl;
    	}
    	else {
    		cout << "Case #" << z << ": " << res << endl;
    	}
    }
    return 0;
}
