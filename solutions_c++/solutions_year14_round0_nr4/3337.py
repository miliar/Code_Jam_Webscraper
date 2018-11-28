#include <cstdio>
#include <algorithm>
using namespace std;
int t, s, reta, retb, akts;
double A [1000], B [1000];
int main () {
	scanf ("%d", &t);
	for (int k = 1; k <= t; k ++) {
		scanf ("%d", &s);
		for (int i = 0; i < s; i ++) scanf ("%lf", &A [i]);
		for (int i = 0; i < s; i ++) scanf ("%lf", &B [i]);
		sort (A, A+s);
		sort (B, B+s);
//		for (int i = 0; i < s; i ++) printf ("%lf\t", A [i]); printf ("\n");
//		for (int i = 0; i < s; i ++) printf ("%lf\t", B [i]); printf ("\n");
	
		//oszukiwana gra
		int ka = s - 1, kb = s - 1;
		reta = 0;
		while (kb >= 0) {
			if (A [ka] > B [kb]) ka --, kb --, reta ++;
			else kb --;
		}

		//normalna gra
		int a = 0, b = 0;
		while (a < s && b < s) {
			while (b < s && A [a] >= B [b]) b ++;
			if (b == s) break;
			a ++;
			b ++;
		}
		retb = s - a;

		printf ("Case #%d: %d %d\n", k, reta, retb);

	}
}
