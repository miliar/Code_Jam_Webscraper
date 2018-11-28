#include<stdio.h>

int main(){
	int T;
	FILE *input_file, *output_file;
	input_file = fopen("A-small-attempt0.in", "r");
	output_file = fopen("output.txt","w");
	fscanf(input_file,"%d",&T);
	for (int i = 0; i < T; i++){
		int s_max;
		int count = 0;
		fscanf(input_file,"%d",&s_max);
		char ch[1002];
		int ch_count[1002];

		for (int j = 0; j < 1002;j++){
			ch_count[j] = 0;
		}

		fscanf(input_file,"%s",ch);

		for (int j = 0; j < s_max + 1;j++){
			if (ch[j]!='0' && j <= ch_count[j]){
				for (int k = j; k < s_max + 1;k++){
					ch_count[k]+=ch[j]-'0';
				}
			}
			else if (ch[j]!='0' && j>ch_count[j]){
				j--;
				ch[j]++;
				count++;
				j--;
			}
		}

		fprintf(output_file,"Case #%d: %d\n",i+1 ,count);
	}
	return 0;
}