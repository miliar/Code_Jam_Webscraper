#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	int t, smax, need, has, tot, j, i;
	scanf("%d", &t);
	for(j = 1; j <= t; j++){
		scanf("%d", &smax);
		char str[1001];
		need = tot = 0;
		has = 0;
		scanf("%s", str);
		//printf("%s", arr);
		int arr[1001] = {0};
		for(i = 0; i <= smax; i++)
			arr[i]= str[i] - 48;
		//printf("%d", arr[0]);
		has = arr[0];
		for(i = 1; i <= smax; i++){
			if(has >= i){
				has += arr[i];
			}
			else{
				need = i - has;
				tot += need;
				has += need + arr[i];
			}
			//printf("%d %d\n",has, need );
		}
		printf("Case #%d: %d\n",j, tot);
	}
	return 0;
}