#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;


int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		char str[1010];
		int k, n;
		scanf ("%s %d", str, &k);

		n = strlen(str);
		int ret = 0;

		for (int i=0;i<=n-k;i++) {
			if (str[i] == '+') {
				continue;
			}
			ret ++;
			for (int j=0;j<k;j++) {
				str[i+j] = (str[i+j]=='+'?'-':'+');
			}
		}

		for (int i=n-k+1;i<n;i++) {
			if (str[i] == '-') {
				ret = -1;
				break;
			}
		}
		printf ("Case #%d: ", tc);

		if (ret == -1) {
			printf ("IMPOSSIBLE\n");
		} else {
			printf ("%d\n", ret);
		}

	}

	return 0;
}