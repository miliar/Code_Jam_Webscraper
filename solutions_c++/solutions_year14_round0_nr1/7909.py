#include<stdio.h>
#include<string.h>

int N[17];

int main(){
	int T;
	int cnt = 0;
	scanf("%d", &T);
	while(T--){
		memset(N, 0, sizeof(N));
		int tmp, g;
		for(int k = 0; k < 2; k++){
			scanf("%d", &tmp);
			for(int i = 0; i < 4; i++){
					for(int j = 0; j < 4; j++){
						scanf("%d", &g);	
						if(i == tmp-1) N[g]++;
					}
			}
		}
		int count = 0;
		int num;
		for(int i = 1; i < 17; i++){
			if(N[i] == 2) count++, num = i;
		}
		printf("Case #%d: ", ++cnt);
		
		if(count == 1){
			printf("%d\n", num);
		}else if(count > 1){
			printf("Bad magician!\n");
		}else{
			printf("Volunteer cheated!\n");
		}
		
	}

	return 0;
}
