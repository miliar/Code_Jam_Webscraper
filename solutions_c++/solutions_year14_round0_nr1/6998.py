#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>


int main(){
	int T,i,j,m,n,count=0,answer;
	int a1,a2;
	int b[4][4],c[4][4];

	FILE *input;
	FILE *output;

	input=fopen("A-small-attempt1.in","r");
	output=fopen("output.txt","w");

	fscanf(input,"%d\n",&T);

	for(i=0;i<T;i++){
		fscanf(input,"%d\n",&a1);

		for(j=0;j<4;j++){
			fscanf(input,"%d %d %d %d\n",&b[j][0],&b[j][1],&b[j][2],&b[j][3]);
		}

		fscanf(input,"%d\n",&a2);

		for(j=0;j<4;j++){
			fscanf(input,"%d %d %d %d\n",&c[j][0],&c[j][1],&c[j][2],&c[j][3]);
		}

		for(m=0;m<4;m++){
			for(n=0;n<4;n++){
				if(b[a1-1][m]==c[a2-1][n]){
					answer=b[a1-1][m];
					count++;
				}
			}
		}

		if(count==1){
			fprintf(output,"Case #%d: %d\n",i+1,answer);
		}
		else if(count==0){
			fprintf(output,"Case #%d: Volunteer cheated!\n",i+1);
		}
		else{
			fprintf(output,"Case #%d: Bad magician!\n",i+1);
		}

		count=0;
	}

	fclose(input);
	fclose(output);

	return 0;
}