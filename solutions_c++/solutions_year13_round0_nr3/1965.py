#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

long long int f[12000005];
bool ispalin(long long int a)
{
	long long int rev = 0;
	long long int tmp = a;

	while (a != 0) {
		rev = rev * 10 + a % 10;
		a /= 10;
	}
	return rev == tmp;
}
int main()
{
	long long int sa, sb, t, a, b, sq, i, u = 1;
	scanf ("%lld", &t);

	int cnt = 0;
	f[0] = 0;
	for (i = 1; i <= 10000000; i++) {
		if (ispalin(i) && ispalin(i * i)) {
			cnt++;
		}
		f[i] = cnt;
	}
	while (t--) {
		cin >> a >> b;
		sa = sqrt(a);
		sb = sqrt(b);
		if (sa * sa == a) {
			a = sa;
		} else {
			a = sa + 1;
		}
		a--;
		b = sb;
		cout << "Case #" << u++ << ": " << f[b] - f[a] << endl;
	}
	/*
	   while (t--) {
	   scanf ("%lld %lld", &a, &b);
	   long long int count = 0;
	   sa = sqrt(a);
	   sb = sqrt(b);
	   if (sa * sa == a) {
	   a = sa;
	   } else {
	   a = sa + 1;
	   }
	   b = sb;
	   for (i = a; i <= b; i++) {
//sq = sqrt(i);
//if (ispalin(i) && ispalin(sq) && sq * sq == i) {
//	count++;
//}
if (ispalin(i) && ispalin(i * i)) {
count++;
}
}
cout << "Case #" << u++ << ": " << count << endl;
}*/
return 0;
}
