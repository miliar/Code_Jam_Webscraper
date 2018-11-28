#include <cstdio>
#include <iostream>
using namespace std;

int er,t, tt, kol, count;
long long x, b[1111], l, r, ans, a[111];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout); 
	scanf("%d", &t);
	tt = t;
	for (int i = 1; i <= 10000000; i++){
		x = (long long)i;
		kol = 0;
		while (x > 0){
			a[++kol] = x % 10;
			x = x / 10;
		}
		er = 0;
		for (int j = 1; j <= kol / 2; j++) if (a[j] != a[kol - j + 1]) er = 1;
		if (er == 1) continue;
		x = (long long)i * i;
		kol = 0;
		while (x > 0){
			a[++kol] = x % 10;
			x = x / 10;
		}
		for (int j = 1; j <= kol / 2; j++) if (a[j] != a[kol - j + 1]) er = 1;
		if (er == 0) b[count++] = (long long)i*i;
	}
	while (t > 0){
		t--;
		cin >> l >> r;
		ans = 0;
		for (int i = 0; i < count; i++) if (b[i] >= l && b[i] <= r) ans++;
		cout << "Case #" << tt - t << ": " << ans << endl;
	}
	return 0;
}