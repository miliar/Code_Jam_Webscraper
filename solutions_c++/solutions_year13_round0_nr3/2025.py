#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


bool palindrome (long long int a)
{
	char z[25];
	int i, j;
	i = 0;
	while (a > 0) {
		z[i++] = a % 10;
		a = a / 10;
	}
	j = 0;
	i--;
	while (j <= i) {
		if (z[j] != z[i]) {
			return false;
		}
		j++;
		i--;
	}

	return true;
}
long long int v[100];
int main ()
{
	long long int a, b, i;
	int t;
	int z;
	int cnt, h = 1, beg, nd;
	int counter = 0;
	scanf ("%d", &t);
	for (long long int i = 1; i < 10000001; i++) {
		if (palindrome (i)) {
			if (palindrome (i * i)) {
				v[counter++] = i*i;
			}
		}
	}
	while (t--) {
		cnt = 0;
		scanf ("%lld %lld", &a, &b);
		beg = 0;
		while (beg < counter && v[beg] < a) {
			beg++;
		}
		nd = beg;
		while (nd < counter && v[nd] <= b) {
			nd++;
		}
		printf ("Case #%d: %d\n", h++, nd - beg);
	}
	
	return 0;
}
