#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<cstring>

using namespace std;

typedef long long ll;
typedef long double ld;

const int MAXN = 200 + 30;
const int XX = 1e7;

int n, k, tt, gec[XX];
ld p[MAXN], d[MAXN][2 * MAXN], sec[MAXN];

ld cal(int mask){
	ld ret = 0;
	int sz = 0;
	for (int i = 0; i < n; i++)
		if ((mask>>i) & 1)	sec[sz++] = p[i];
	for (int i = 0; i < tt; i++){
		mask = gec[i];
		ld temp = 1;
		for (int j = 0; j < k; j++)
			if ((mask >> j) & 1)
				temp *= sec[j];
			else
				temp *= 1. - sec[j];
		ret += temp;
	}
	return ret;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout << fixed << setprecision(8);
	int te;	cin >> te;
	for (int t = 1; t <= te; t++){
		cin >> n >> k;
		tt = 0;
		for (int i = 0; i < (1<<k); i++)
			if (__builtin_popcount(i) == k/2)
				gec[tt++] = i;
		for (int i = 0; i < n; i++)	cin >> p[i];
		sort(p, p + n);

		ld mx = 0;
		for (int i = 0; i < (1<<n); i++)
			if (__builtin_popcount(i) == k)
				mx = max(mx, cal(i));

		cout << "Case #" << t << ": ";
		cout << mx << "\n";
	}
	return 0;
}
