#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int qnumber, answer, i, j, k;
	char array[256];
	FILE *q=fopen("B-large.in","r");
	FILE *result=fopen("result.out", "w");
	fscanf(q,"%d", &qnumber);
	for(i=1;i<=qnumber;i++){
		answer=0;
		fscanf(q, "%s", array);
		if(array[0]==45){
				answer=answer+1;
		}
		k=strlen(array);
		for(j=0;j<k;j++){
			if(array[j-1]==43 && array[j]==45){
				answer=answer+2;
			}
		}
	fprintf(result, "Case #%d: %d\n",i ,answer);
	}
fclose(result);
return 0;
}
