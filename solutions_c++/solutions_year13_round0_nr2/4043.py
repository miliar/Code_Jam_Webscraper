#include <stdio.h>

int main(){
	FILE *input;
	FILE *output;
	input=fopen("B-large.in", "r");
	output=fopen("output.txt", "w");
	int cases;
	int n,m,flag;
	int field[100][100];
	fscanf(input, "%d", &cases);
	for(int c=0;c<cases;c++){
		fscanf(input, "%d %d", &n, &m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				fscanf(input, "%d", &field[i][j]);
			}
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				flag=0;
				//checkrow;
				for(int k=0;k<m;k++){
					if(field[i][k]>field[i][j]){
						flag=1;
					}
				}
				for(int k=0;k<n;k++){
					if(field[k][j]>field[i][j] && flag==1){
						flag=2;
					}
				}
				if(flag==2){
					fprintf(output, "Case #%d: NO\n", c+1);
					i=n;
					j=m;
				}
			}
		}
		if(flag!=2){
			fprintf(output, "Case #%d: YES\n", c+1);
		}

	}
	fclose(input);
	fclose(output);
	return 0;
}