#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int M = 1005;
double str1[M], str2[M];

int main () {
	
	int t, n, i, j, k;
	int s1 , s2;
	scanf ("%d", &t);
	for ( k = 1; k <= t; k++) {
	
		s1 = s2 = 0;
		scanf ("%d", &n);
		for ( i = 0; i < n; i++)
			scanf ("%lf", &str1[i]);
		for ( i = 0; i < n; i++)
			scanf ("%lf", &str2[i]);
		sort (str1, str1 + n);
		sort (str2, str2 + n);

		i = j = 0;
		while (i != n && j != n) {

			if (str1[i] > str2[j])
				j++;
			else {
				i++;
				j++;
			}
		}
		 s2 = j - i;
		 int a = 0, b = n - 1;
		 j = n - 1;
		 while (a <= b) {

			if (str1[b] < str2[j]) {
				a++;
				j--;
			}
			else {
				j--;
				b--;
				s1++;
			}
		 }
		 printf ("Case #%d: %d %d\n", k, s1, s2);
	}
	return 0;
}
