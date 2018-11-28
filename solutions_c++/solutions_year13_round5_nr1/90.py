#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int n;
vector <long long> x;
long long sum[38];
long long b;

void Load()
{
	cin >> b >> n;
	int i;
	x.clear();
	x.resize(37);
	for (i = 0; i < n; i++)
		cin >> x[i];
	sort(x.begin(), x.end());
	sum[0] = x[0];
	for (i = 1; i < 37; i++)
		sum[i] = x[i] + sum[i-1];
}


long long calc(int i, long long h) {
	int l = 0;
	while (i + l + 1 < 37 && x[i+l+1] <= h) l++;
//    cerr << "calc " << i << ' ' << h << " " << h * (i+1) + (h+1) * l - sum[i+l] <<"\n";
	return h * (i+1) + (h+1) * l - sum[i+l];
}

long long findMax(int i) {
	long long l = x[i];
	long long r = 100000000000000LL;
	long long ans = -1;
//	cerr << "findmax " << i << "\n";
	while (l <= r) {
		long long m = (l + r) / 2;
        long long need = calc(i, m);
//        cerr << "for mid " << m << " got " << need << "\n";
		if (need <= b) {
			l = m+1;
			if (m > ans)
				ans = m;
		} else {
			r = m-1;
		}
	}
	return ans;	
}

void Solve()
{
	int i;
	long long h;
	long double ans = 0;
	calc(35,10);
	for (i = 0; i < 37; i++) {
		h = findMax(i);
//		cerr << "for x[i] " << x[i] << " has height " << h << "\n";
		if (h < 0) continue;
		long double cur = ((long double) h*(i+1) - sum[i])*36.0 / (i+1) - calc(i, h);
//		cerr << "profit " << cur << "\n";
		if (cur > ans)
			ans = cur;
	}
	cout << ans << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
