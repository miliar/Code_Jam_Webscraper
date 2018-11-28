#include <iostream>
#include <cmath>

using namespace std;

int n;
int p;
int a[100000];
int b[15][3];
int r;
int e[100000];
int g;

void mkPalind ()
{
	int m;
	int i;
	int j;
	int k;

	if (n > 5) {
		return;
	}

	b[r][0] = p;
	for (i = 1; i < 10; i++) {
		for (m = n / 2, k = 0; m < n; m++, k++) {
//		for (i = 1; i < 10; i++) {
//			a[p] = (i * pow (10, m)) + i;
//			p++;

			for (j = b[k][0]; j < b[k][1]; j++) {
				a[p] = (i * pow (10, m) + a[j]) * pow (10, n - m) + i;
				p++;
			}
		}
	}
//	b[r][0] = b[r - 1][2];
	b[r][1] = p;

	n++;
	for (i = 1; i < 10; i++) {
		a[p] = (i * pow (10, n)) + i;
		p++;

		for (m = n / 2 + 1, k = 0; m < n; m++, k++) {
//		for (i = 1; i < 10; i++) {
//			a[p] = (i * pow (10, m)) + i;
//			p++;

			for (j = b[k][1]; j < b[k][2]; j++) {
				a[p] = (i * pow (10, m) + a[j]) * pow (10, n - m) + i;
				p++;
			}
		}
	}
	b[r][2] = p;
	n++;
	r++;

	mkPalind ();
}

void fn ()
{
	int i;
	int k;
	int s;
	int q;

	for (i = 1; i < p; i++) {
		k = a[i] * a[i];

		s = k;
		q = 0;
		while (k > 0) {
			q = q * 10 + (k % 10);
			k = k / 10;
		}

		if (q == s) {
			e[g] = s;
			g++;
		}
	}
}

int main()
{
	int i;
	int c;
	int d;
	int j;
	int k;
	int t;

	a[0] = 0;
	a[1] = 1;
	a[2] = 2;
	a[3] = 3;
	a[4] = 4;
	a[5] = 5;
	a[6] = 6;
	a[7] = 7;
	a[8] = 8;
	a[9] = 9;
	a[10] = 11;
	a[11] = 22;
	a[12] = 33;
	a[13] = 44;
	a[14] = 55;
	a[15] = 66;
	a[16] = 77;
	a[17] = 88;
	a[18] = 99;
	b[0][0] = 0;
	b[0][1] = 10;
	b[0][2] = 19;
	n = 2;
	r = 1;
	p = 19;
	g = 0;

	mkPalind  ();
	fn ();

/*	for (i = 0; i < g; i++) {
		cout << e[i] << '\n';
	}
*/
	k = 1;
	cin >> t;

	while (k <= t) {
	cin >> c >> d;

//	c = sqrt (c);
//	d = sqrt (d);

	j = 0;
	for (i = 0; i < 6; i++) {
		if (e[i] >= c && e[i] <= d) {
			j++;
		}
	}

	cout << "Case #" << k << ": " << j << endl;
	k++;
	}

	return 0;
}
