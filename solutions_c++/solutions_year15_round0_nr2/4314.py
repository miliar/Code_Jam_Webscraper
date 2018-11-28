#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int n, v[1024];

int main() {
	int t, test = 1;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		
		int sum = 0;
		for(int i=0; i<n; i++) {
			scanf("%d", &v[i]);
			sum += v[i];
		}
		
		int ans = 1000000000;
		for(int i=1; i<=sum; i++) {
			int count = 0;
			for(int j=0; j<n; j++) {
				count += (int)ceil(double(v[j])/double(i))-1;
			}
			ans = min(ans, count+i);
		}
		printf("Case #%d: %d\n", test++, ans);
	}
}
