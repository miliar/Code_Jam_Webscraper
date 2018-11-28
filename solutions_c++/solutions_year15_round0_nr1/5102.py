#include <stdio.h>
int main(){
	int T;
	scanf("%d", &T);
	for (int i=1; i<=T; i++){
		int n;
		int arr[1001] = { 0, };
		scanf("%d", &n);
		for (int j = 0; j <= n; j++){
			scanf(" %c", &arr[j]);
			arr[j] -= '0';
		}
		int sol = 0;
		int temp = 0;
		for (int j = 0; j < n; j++){
			temp += arr[j];
			if (temp+sol < j+1){
				sol = j+1 - temp;
			}
		}
		printf("Case #%d: %d\n", i,sol);
	}
}