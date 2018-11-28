#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MXN = 1000;

double a[MXN], b[MXN];
int n;

int dans, wans;

void dew()
{
	int i = 0, ii = n, j = n - 1;
	dans = 0;
	while (i < ii) {
		if (a[ii - 1] > b[j]) {
			--ii;
			++dans;
		}
		else {
			++i;
		}
		--j;
	}
}

void war()
{
	wans = 0;
	int i = n - 1, j = n - 1;
	while (i >= 0) {
		if (a[i] < b[j]) {
			--j;
		}
		else {
			++wans;
		}
		--i;
	}
}

void deal()
{
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	sort(a, a + n);

	for (int i = 0; i < n; ++i) {
		cin >> b[i];
	}
	sort(b, b + n);

	dew();
	war();

	cout << dans << ' ' << wans << endl;
}

int main()
{
	int cases;

	ios::sync_with_stdio(false);

	cin >> cases;
	for (int t = 1; t <= cases; ++t) {
		cout << "Case #" << t << ": ";
		deal();
	}

	return 0;
}