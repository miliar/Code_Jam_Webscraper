#include<stdio.h>

FILE*in=fopen("A-large.IN","r");
FILE*out=fopen("output.txt","w");

int main(){
	int num,large,check,people,j,i;
	char str[123456];
	fscanf(in,"%d", &num);

	for (i = 0; i < num; i++){
		check = 0, people = 0;
		fscanf(in,"%d %s", &large, str);

		for (j = 0; j <=large; j++){
			if (people < j){
				check += (j - people);
				people=j;
			}
			people += (str[j]-48);
		}
		fprintf(out,"Case #%d: %d\n",i+1, check);
	}
	return 0;
}
