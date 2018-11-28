#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 2000;
int t, n;
double x[maxn], y[maxn];

int main()
{
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n;
		for (int i = 0; i < n; i++) cin >> x[i];
		sort(x,x+n);
		for (int i = 0; i < n; i++) cin >> y[i];
		sort(y,y+n);
		int a = 0, b = n;
		for (int i = 0; i < n; i++) {
			if (x[i] > y[a]) ++a;
		}
		for (int i = 0; i < n; i++) {
			if (x[n-b] < y[i]) --b;
		}
		cout << "Case #" << ca<< ": ";
		cout << a << ' ' << b << endl;
	}
	return 0;
}

