#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>
#include <map>

using namespace std;
typedef long long ll;
typedef pair<int,int> pr;

int main()
{
	// code here
	int T;
	scanf("%d", &T);
	for (int tc=1; tc<=T; tc++) {
		int n;
		double naomi[1000], ken[1000];
		int deceitful = 0, normal = 0;
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			scanf("%lf", naomi+i);
		}
		for (int i=0; i<n; i++) {
			scanf("%lf", ken+i);
		}
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		int i=0, j=0;
		while (i < n && j < n) {
			if (ken[j] < naomi[i]) {
				deceitful++;
				i++, j++;
			}
			else {
				i++;
			}
		}
		i=0, j=0;
		while (i < n && j < n) {
			if (naomi[i] < ken[j]) {
				normal++;
				i++, j++;
			}
			else {
				j++;
			}
		}

		printf("Case #%d: %d %d\n", tc, deceitful, n-normal);
	}

	// code ends here
	return 0;
}
