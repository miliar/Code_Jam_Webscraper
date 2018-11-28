#include <stdio.h>

int main(){
	int t;
	scanf(" %d", &t);
	for(int k = 1; k <= t; k++){
		bool seen[10];
		for(int i = 0; i < 10; i++){
			seen[i] = false;
		}
		int val;
		scanf(" %d", &val);
		if(val == 0){
			printf("Case #%d: INSOMNIA\n", k);
			continue;
		}
		int orig = val;
		while(true){
			int aux = val;
			while(aux != 0){
				seen[aux%10] = true;
				//printf("Seen[%d], val = %d\n", aux%10, val);
				aux/=10;
			}
			bool teste = true;
			for(int i = 0; i < 10; i++){
				if(!seen[i]){
					teste = false;
					break;
				}
			}
			if(teste)
				break;
			val+=orig;
		}
		printf("Case #%d: %d\n", k, val);
	}
	return 0;
}