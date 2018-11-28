#include<iostream>
using namespace std;

int testcases;
bool f[17];

int main() {
	scanf("%d", &testcases);
	for (int t = 0; t < testcases; t++) {
		int x;
		scanf("%d", &x);
		x --;
		for (int i = 1; i <= 16; i++)
			f[i] = false;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++) {
				int n;
				scanf("%d", &n);
				if (i == x)
					f[n] = true;
			}		
		scanf("%d", &x);
		x --;
		int tot = 0;	
		int ans = 0;	
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++) {
				int n;
				scanf("%d", &n);
				if (i == x && f[n]) {
					tot ++;
					ans = n;
				}
			}		
		printf("Case #%d: ", t + 1);
		if (tot == 1)
			printf("%d", ans);
		else if (tot == 0)
			printf("Volunteer cheated!");
		else 
			printf("Bad magician!");
		printf("\n");
	}
	return 0;
}