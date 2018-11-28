#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;

int ms[100000],used[100000],lens[100000];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int q=0; q<t; q++) {
		int n,x;
		scanf("%d%d",&n,&x);
		for (int j=0; j<1000; j++) {
			ms[j] = x;
			used[j] = 0;
		}
		for (int i=0; i<n; i++)
			scanf("%d",&lens[i]);
		sort(lens,lens+n);
		for (int i=n-1; i>=0; i--) {
			int AA = lens[i];
			for (int j=0; j<1000; j++)
				if (ms[j] >= AA && used[j] < 2) {
					ms[j]-=AA;
					used[j]++;
					break;
				}
		}
		int cnt = 0;
		for (int j=0; j<1000; j++)
			if (ms[j]!=x) cnt++;
		printf("Case #%d: %d\n",q+1,cnt);
	}

	return 0;
}