#include <bits/stdc++.h>

using namespace std;

int t,s,p,n,m;
char c[1002];

int main(void){
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d", &s);
		scanf("%s", c);
		n = m = 0;
		for (int j = 0; j <= s; j++){
			p = c[j] - '0';
			if (n >= j)
				n += p;
			else 
				m += j-n, n = j+p;
		}		
		printf("Case #%d: %d\n", i, m);
	}
	return 0;
}
