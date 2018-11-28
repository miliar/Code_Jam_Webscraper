#include <stdio.h>
#include <string.h>

int main(){
	int tc;
	int count, i, j;
	long long int num, n, len;
	char data[100];
	int check[10];
	FILE* fp = fopen("output.txt", "w");
	
	scanf("%d", &tc);
	
	for(count = 0; count < tc; count++){
		scanf("%d", &num);
		if(num == 0){
			fprintf(fp, "Case #%d: INSOMNIA\n", count+1);
			printf("Case #%d: INSOMNIA\n", count+1);
			continue;
		}
		n = 0;
		for(i = 0; i < 10; i++)
			check[i] = 0;
		j = 0;
		while(j != 10){
			n += num;
			sprintf(data, "%d", n);
			len = strlen(data);
			for(i = 0; i < len; i++){
				if(check[data[i] - '0'] == 0){
					j++;
					check[data[i] - '0'] = 1;
				}
				if(j == 10)
					break;
			}
		}
		
		fprintf(fp, "Case #%d: %d\n", count+1, n);
		printf("Case #%d: %d\n", count+1, n);
	}
}
