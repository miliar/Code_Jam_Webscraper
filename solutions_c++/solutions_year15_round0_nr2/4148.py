#include <bits/stdc++.h>

using namespace std;

int t,d,p[1000],s,q;

int main(void){
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d", &d);
		for (int j = 0; j < d; j++)
			scanf("%d", &p[j]);
		s = 1000000000;
		for (int j = 1; j <= 1000; j++){
			q = 0;
			for (int k = 0; k < d; k++)
				if (p[k] > j)
					q += (p[k]+j-1)/j-1;
			s = min(s, q + j);
		}
		printf("Case #%d: %d\n", i, s);
	}
	return 0;
}
