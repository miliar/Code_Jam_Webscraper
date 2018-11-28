#include <bits/stdc++.h>
using namespace std;

int A[10];

void digits(int u) {
	while(u>0) {
		A[u%10] = 1;
		u /= 10;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc=1; tc<=t; tc++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", tc);
		if(n==0) {
			printf("INSOMNIA\n");
		}
		else{
			memset(A, 0, sizeof A);
			int final = -1;
			for(int i=1; i<=1000; i++) {
				int num = i*n;
				digits(num);
				int yes = 1;
				for(int i=0; i<10; i++)
					yes &= A[i];
				if(yes)  {	
					final = num;
					break;
				} 
			}
			if(final == -1) {
				printf("INSOMNIA\n");
			}
			else {
				printf("%d\n", final);
			}
		}
	}
}