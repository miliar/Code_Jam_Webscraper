#include <bits/stdc++.h>
using namespace std;

int main(){
	char s[1010]; int shymax, t;
	unsigned long int tmp, current; scanf("%d", &t);
	for(int i=1; i<=t; i++){
		tmp = 0; current = 0;
		scanf("%d %s", &shymax, s);
		for(int j=0; j<=shymax; j++){
			if(current<j) {
				tmp += j-current;
				current += j-current;
			}
			current += s[j] - '0';
		}
		printf("Case #%d: %lu\n", i, tmp);
	}
}