#include <bits/stdc++.h>

using namespace std;


#define long long long

const int mod = 1000000007;
const int M = 120;

int r, c;
long d[M][8][M];

void read() {
	cin >> r >> c;
}

bool has(int mask, int c) {
	return (mask >> (c - 1)) & 1;
}

int get(int a, int b = -1) {
	if (b == -1)
		return 1 << (a - 1);
	return (1 << (a - 1)) | (1 << (b - 1));
}

long bin(long x, long a) {
	long y = 1;
	while (a) {
		if (a & 1)
			y = (y * x) % mod;
		x = (x * x) % mod;
		a >>= 1;
	}
	return y;
}

void kill() {
	for (int i = 0; i <= r; ++i)
		for (int mask = 0; mask < 8; ++mask)
			for (int shift = 0; shift < c; ++shift)
				d[i][mask][shift] = 0;

	for (int shift = 0; shift < c; ++shift)
		d[0][0][shift] = 1;

	for (int i = 0; i <= r; ++i)
		for (int mask = 0; mask < 8; ++mask)
			for (int shift = 0; shift < c; ++shift) {

				d[i][mask][shift] %= mod;
				
				/*
					333333
					333333
				*/
				if (!has(mask, 3))
					d[i + 2][get(3)][shift] += d[i][mask][shift]; 

				/*
					222222
				*/
				if (!has(mask, 2))
					d[i + 1][get(2)][shift] += d[i][mask][shift];

				/*
					211222
					222211
				*/
				if (!has(mask, 2) && !has(mask, 1) && c % 6 == 0 && shift % 6 == 0)
					d[i + 2][get(2, 1)][shift] += 6 * d[i][mask][shift];

				/*
					221221
					221221 ...
				*/
				if (!has(mask, 2) && !has(mask, 1) && c % 3 == 0 && shift % 3 == 0)
					d[i + 2][get(2, 1)][shift] += 3 * d[i][mask][shift];

				/*
					2122
					2121
					2221
				*/
				if (!has(mask, 2) && !has(mask, 1) && c % 4 == 0 && shift % 4 == 0)
					d[i + 3][get(2, 1)][shift] += 4 * d[i][mask][shift];
			}

	long sum = 0;
	for (int mask = 0; mask < 8; ++mask)
		for (int shift = 0; shift < c; ++shift) {
			sum += d[r][mask][shift];
			sum %= mod;
		}
	sum %= mod;
	sum = (sum * bin(c, mod - 2)) % mod;
	cout << sum << "\n";
}

int main() {
	cout.precision(9);
	cout << fixed;
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		read();
		cout << "Case #" << i << ": ";
		kill();
	}
}