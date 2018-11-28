#include <stdio.h>

int main(){
	int cases;
	FILE *input;
	FILE *output;
	input=fopen("C-small-attempt1.in","r");
	output=fopen("output.txt", "w");
	int num,a,b;
	fscanf(input, "%d", &cases);
	int pal[5];
	pal[0]=1;
	pal[1]=4;
	pal[2]=121;
	pal[3]=484;
	pal[4]=9;
	for(int c=0;c<cases;c++){
		num=0;
		fscanf(input, "%d %d", &a,&b);
		for(int i=0;i<5;i++){
			if(pal[i]>=a && pal[i]<=b){
				num++;
			}
		}



		fprintf(output, "Case #%d: %d\n", c+1,num);
	}
	fclose(input);
	fclose(output);
	return 0;
}