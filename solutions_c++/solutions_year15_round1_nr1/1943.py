#include <bits/stdc++.h>

using namespace std;

int t,n,m[1000],p,q,r;

int main(void){
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%d", &m[j]);
		p = q = r = 0;
		for (int j = 1; j < n; j++){
			if (m[j] < m[j-1])
				p += m[j-1]-m[j];
			r = max(r, m[j-1]-m[j]);
		}
		for (int j = 0; j < n-1; j++)
			q += min(r, m[j]);
			
		printf("Case #%d: %d %d\n", i, p, q);
	}
	return 0;
}
