#include <cstdio>
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		int n;
		scanf("%d", &n);
		int m[n], a1 = 0, a2 = 0, maxdiff = 0;
		scanf("%d", &m[0]);
		for(int i=1; i<n; i++){
			scanf("%d", &m[i]);
			int diff = m[i-1] - m[i];
			if(diff > 0){
				a1 += diff;
				if(diff > maxdiff) maxdiff = diff;
			}
		}
		for(int i=0; i<n-1; i++){
			if(m[i] < maxdiff) a2 += m[i];
			else a2 += maxdiff;
		}
		printf("Case #%d: %d %d\n", i, a1, a2);
	}
	return 0;
}