#include <stdio.h>
#include <string.h>

int main(){
	int tc;
	int count, i, num, n;
	int  len;
	char data[101];
	char start, tmp;
	FILE* fp = fopen("output.txt", "w");
	
	scanf("%d", &tc);
	
	for(count = 0; count < tc; count++){
		scanf("%s", data);
		num = 0;
		len = strlen(data);
		while(true){
			n = 1;
			start = data[0];
			for(i = 1; i < len; i++){
				if(data[i] == start)
					n++;
				else
					break;
			}
			if(start == '+' && n == len)
				break;
				
			num++;
			tmp = (start=='-'? '+':'-');
			for(i = 0; i < n; i++){
				data[i] = tmp;
			}
		}
		fprintf(fp, "Case #%d: %d\n", count+1, num);
		printf("Case #%d: %d\n", count+1, num);
	}
}
