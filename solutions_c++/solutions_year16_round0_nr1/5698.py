#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int nn;
	scanf("%d\n", &nn);
	for(int cc=1; cc<=nn; cc++) {
		printf("Case #%d: ", cc);
		
		bool V[10];
		for(int i=0; i<10; i++) {
			V[i] = false;
		}
		
		int n;
		scanf("%d\n", &n);
		
		if(n == 0) {
			printf("INSOMNIA\n");
		}
		else {
			int i = n;
			while(true) {
				int t = i; // temp
				while(t > 0) {
					int d = t % 10;
					V[d] = true;
					t /= 10;
				}
				bool v = true;
				for(int j=0; j<10; j++) {
					if(!V[j]) {
						v = false;
						break;
					}
				}
				if(v) {
					printf("%d\n", i);
					break;
				}
				i += n;
			}
		}
	}
	
	return 0;
}
