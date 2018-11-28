#include <stdio.h>
#pragma warning(disable:4996)
int t;
int smax;
int s[1010];
int sum;
int frnd;
int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d", &t);
	int i, k = 1;
	while (t--){
		sum = 0;
		frnd = 0;
		scanf("%d", &smax);
		for (i = 0; i <= smax; i++){
			scanf("%1d", &s[i]);
			if (sum < i && s[i]){
				frnd += i - sum;
				sum += s[i] + frnd;
			}
			else sum += s[i];
		}
		printf("Case #%d: %d\n", k, frnd);
		k++;
	}
	return 0;
}