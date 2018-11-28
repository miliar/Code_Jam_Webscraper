#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t, n;
	scanf ("%d", &t);
	char x[111];


	for (int tc=1;tc<=t;tc++) {
		scanf ("%s", x);
		n = strlen (x);
		int cur = 0, ans = 0;
		for (int i=n-1;i>=0;i--) {
			if (x[i] == '-') {
				if (!cur) {
					ans ++;
					cur = 1;
				}
			} else {
				if (cur) {
					ans ++;
					cur = 0;
				}
			}
		}
		printf ("Case #%d: %d\n", tc, ans);
	}


	return 0;
}