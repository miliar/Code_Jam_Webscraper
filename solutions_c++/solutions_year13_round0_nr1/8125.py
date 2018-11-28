#include<stdio.h>
#include<memory.h>

#define N 4

FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

char data[N+10][N+10], n;

void process(int c){
	int i, j, k;
	bool flag;
	char translate[3] = "OX";
	memset(data,0,sizeof(data));
	for(i=0;i<N;i++)
		fscanf(in,"%s",&data[i]);
	for(i=0;i<N;i++){
		for(k=0;k<2;k++){
			flag = true;
			for(j=0;j<N;j++){
				if(data[i][j] != translate[k] && data[i][j] != 'T'){
					flag = false;
					break;
				}
			}
			if(flag == true){
				fprintf(out,"Case #%d: %c won\n",c,translate[k]);
				return;
			}
			flag = true;
			for(j=0;j<N;j++){
				if(data[j][i] != translate[k] && data[i][j] != 'T'){
					flag = false;
					break;
				}
			}
			if(flag == true){
				fprintf(out,"Case #%d: %c won\n",c,translate[k]);
				return;
			}
		}
	}
	for(k=0;k<2;k++){
		flag = true;
		for(j=0;j<N;j++){
			if(data[j][j] != translate[k] && data[i][j] != 'T'){
				flag = false;
				break;
			}
		}
		if(flag == true){
			fprintf(out,"Case #%d: %c won\n",c,translate[k]);
			return;
		}
	}
	for(k=0;k<2;k++){
		flag = true;
		for(j=0;j<N;j++){
			if(data[j][N-1-j] != translate[k] && data[j][N-1-j] != 'T'){
				flag = false;
				break;
			}
		}
		if(flag == true){
			fprintf(out,"Case #%d: %c won\n",c,translate[k]);
			return;
		}
	}

	flag = true;
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			if(data[i][j] == '.'){
				fprintf(out,"Case #%d: Game has not completed\n",c,translate[k]);
				return;
			}
		}
	}
	fprintf(out,"Case #%d: Draw\n",c,translate[k]);
}

int main(){
	int i, j;
	fscanf(in,"%d",&j);
	for(i=0;i<j;i++)
		process(i+1);
	fclose(in);
	fclose(out);
	return 0;
}