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

	int n, t;
	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		scanf ("%d", &n);
		printf ("Case #%d: ",tc);
		if (n) {
			int rem = 10, i;
			bool vis[10] = {false};
			for (i=n;rem;i+=n) {
				int c = i;
				while (c) {
					if (!vis[c%10]) {
						vis[c%10] = true;
						rem --;
					}
					c /= 10;
				}
			}
			printf ("%d\n", i-n);
		} else {
			printf("INSOMNIA\n");
		}
	}

	return 0;
}