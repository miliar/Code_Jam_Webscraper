#include <iostream>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second

using namespace std;

long long a[2000000];
int n;

long long f(int l, int r){
	return max(a[n] - a[r], max(a[r] - a[l - 1], a[l - 1]));
}

int main(){
	freopen("inputa2.in","r",stdin);
	freopen("outputa2.out","w",stdout);
	int T;
	cin >> T;
	cout << fixed << setprecision(15);
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
		
		long long p, q, r, s;
				
		cin >> n >> p >> q >> r >> s;

		for (int i = 1; i <= n; i++){
			a[i] = (p * (i - 1) + q) % r + s;
			a[i] = a[i - 1] + a[i];			
		}

		int rr = 1;
		long long ans = a[n] - f(1, 1);
		for (int l = 1; l <= n; l++){
			while ((rr < n) && (f(l, rr) > f(l, rr + 1))) rr++;

			ans = max(ans, a[n] - f(l, rr));
		}
		cout << (ans + 0.0) / (a[n] + 0.0) << endl;
	}
    return 0;
}
