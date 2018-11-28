#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

int a[1024];

int main() {
int c;
	scanf("%d",&c);
	for (int z = 1; z <= c; ++z) {
		int n;
		scanf("%d", &n);
		int m = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", a + i);
			m = max(m, a[i]);
		}
		int answer = m;
		for (int i = 1; i < m; ++i) {
			int may = i;
			for (int j = 0; (may < answer) && (j < n); ++j) {
				may += (a[j]  + i - 1) / i - 1;
			}
			answer = min(answer, may);
		}
		printf("Case #%d: %d\n",z,answer);
	}
	return 0;
}
		
