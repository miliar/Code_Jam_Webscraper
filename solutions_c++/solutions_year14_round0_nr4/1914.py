#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

const int maxn=1005;
const double eps=1e-8;

double a[maxn],b[maxn];

int main() {
	int cases;
	scanf("%d",&cases);
	for (int o=0; o<cases; ++o) {
		int n;
		scanf("%d",&n);
		for (int i=0; i<n; ++i) {
			scanf("%lf",&a[i]);
		}
		sort(a,a+n);
		for (int i=0; i<n; ++i) {
			scanf("%lf",&b[i]);
		}
		sort(b,b+n);
		int ans=0, i=n-1;
		for (int j=n-1; j>=0; --j) {
			while (i>=0&&b[i]>a[j]+eps) --i;
			if (i>=0&&a[j]>b[i]+eps) {
				++ans;
				--i;
			}
			if (i==-1) break;
		}
		printf("Case #%d: %d ",o+1,ans);
		ans=0;
		i=n-1;
		for (int j=n-1; j>=0; --j) {
			while (i>=0&&a[i]>b[j]+eps) --i;
			if (i>=0&&b[j]>a[i]+eps) {
				++ans;
				--i;
			}
			if (i==-1) break;
		}
		printf("%d\n",n-ans);
	}
	return 0;
}

