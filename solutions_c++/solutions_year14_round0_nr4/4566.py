#include <bits/stdc++.h>

using namespace std;

vector<int> solve()
{
	int n;
	double a[1024], b[1024];
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) scanf("%lf", a + i);
	for (int i = 0; i < n; i++) scanf("%lf", b + i);
	
	sort(a, a + n); reverse(a, a + n);
	sort(b, b + n); reverse(b, b + n);
	
	vector<int> ret(2, 0);
	
	ret[1] = n;
	int idx = 0;
	for (int i = 0; i < n; i++){
		while (idx < n && b[i] < a[idx]) idx++;
		if (idx < n) {idx++; ret[1]--;}
	}
	
	int maxi = 0;
	for (int ex = 0; ex < n; ex++){
		int ct = 0;
		for (int i = 0; i < n - ex; i++){
			if (a[i] > b[i + ex]) ct++;
		}
		maxi = max(maxi, ct);
	}
	
	ret[0] = maxi;
	
	return (ret);
}

int main()
{
	int Tnum;
	
	scanf("%d", &Tnum);
	
	for (int i = 0; i < Tnum; i++){
		vector<int> ret = solve();
		printf("Case #%d: %d %d\n", i + 1, ret[0], ret[1]);
	}
	return (0);
}