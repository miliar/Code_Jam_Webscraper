
#include<bits/stdc++.h>
#include <pthread.h>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);

	int n, x, f, c, k;
	scanf("%d", &n);
	int taken[10];
	int counter = 1;
	for(int i = 0; i < n; i++) {
		scanf("%d", &x);
		printf("Case #%d: ", counter++);
		if(x == 0) {
			printf("INSOMNIA\n");
		}
		else {
			memset(taken, 0, sizeof(taken));
			c = 0;
			k = 0;
			while(c != 10) {
				k++;
				f = k * x;
				while(f != 0) {
					if(taken[f % 10] == 0) {
						taken[f % 10] = 1;
						c++;
					}
					f /= 10;
				}
			}
			printf("%d\n", k * x);
		}
	}
	return 0;
}

















