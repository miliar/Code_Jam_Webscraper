#include<stdio.h>

int nt;
int maxShyness;
char tempShyness[1010];
int arrShyness[1010];

int main(){
	scanf("%d", &nt);
	for(int t=0; t<nt; t++){
		scanf("%d %s", &maxShyness, &tempShyness);

		for(int i=0; i<=maxShyness; i++){
			arrShyness[i] = tempShyness[i] - '0';
		}

		int result = 0;
		int now = arrShyness[0];
		for(int i=1; i<=maxShyness; i++){
			if(now < i){
				int diff = i - now;
				result += diff;
				now += arrShyness[i] + diff;
			}
			else{
				now += arrShyness[i];
			}
		}

		printf("Case #%d: %d\n", t+1, result);
	}
	return 0;
}