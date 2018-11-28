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

int a[100000];

int main() {
	int cases;
	scanf("%d",&cases);
	for (int o=0; o<cases; ++o) {
		printf("Case #%d: ",o+1);
		int n,m;
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; ++i) {
			scanf("%d",&a[i]);
		}
		sort(a,a+n);
		int head=0, tail=n-1, ans=0;
		while (head<=tail) {
			if (head==tail) {
				++ans;
				++head;
				--tail;
			} else if (a[head]+a[tail]>m) {
				--tail;
				++ans;
			} else {
				++ans;
				++head;
				--tail;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}