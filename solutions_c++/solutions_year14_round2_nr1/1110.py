#include<stdio.h>
#include<math.h>
#include<string.h>
#define IN in
#define OUT out

int main(void)
{
//	FILE *in = fopen("input.txt","r");
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");

	int T;	
	fscanf(in,"%d",&T);
	for(int t = 0; t < T ; t++)
	{
		int n;
		char str[101][101];

		char std_str[101];
		fscanf(in,"%d",&n);
		for(int i = 0; i < n; i++)
		{
			fscanf(in,"%s",str[i]);
		}
				
		int N = 0;
		int win = -1;
		std_str[0] = str[0][0];
		for(int i = 1; i < strlen(str[0]); i++)
		{
			if(std_str[N] != str[0][i]) std_str[++N] = str[0][i];
		}
		std_str[++N] = '\0';
//		printf("%s\n",std_str);

		for(int i = 0; i < n; i++)
		{
			char tmp_str = str[i][0];
			int tN = 0;
			if(tmp_str != std_str[0]){
				win = 1;
				break;
			}
			for(int j = 1; j < strlen(str[i]); j++)
			{
				if(tmp_str != str[i][j]){
					tmp_str = str[i][j];
					tN++;
					if(tmp_str != std_str[tN]){
						win = 1;
						break;
					}					
				}
			}
			tN++;
			if(tN != N) win = 1;
			if(win == 1) break;
		}

		if(win == 1) fprintf(OUT,"Case #%d: Fegla Won\n",t + 1);
		else{
			int word_len[101][101];
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < N; j++)
					word_len[i][j] = 0;
			}

			for(int i = 0; i < n; i++)
			{
				int cnt = 1;
				int k = 0;
				for(int j = 1; j < strlen(str[i]); j++)
				{
					if(j > 0 && str[i][j - 1] != str[i][j]){
						word_len[i][k++] = cnt;
						cnt = 1;
					}
					else cnt++;
				}
				word_len[i][k++] = cnt;
			}
			/*			
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < N; j++)
				{
					printf("%d ",word_len[i][j]);
				}
				printf("\n");
			}
			*/
			for(int p = 0; p < N; p++)
			{
				for(int i = 0; i < n; i++)
				{
					for(int j = 0; j < n; j++)
					{
						int temp;
						if(word_len[i][p] < word_len[j][p]){
							temp = word_len[i][p];
							word_len[i][p] = word_len[j][p];
							word_len[j][p] = temp;
						}
					}
				}
			}
			/*
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < N; j++)
				{
					printf("%d ",word_len[i][j]);
				}
				printf("\n");
			}
			*/

			int mid = n / 2;
			int tot = 0;
			for(int i = 0; i < N; i++)
			{
				for(int j = 0; j < n; j++)
				{
					tot += abs(word_len[mid][i] - word_len[j][i]);
				}
			}
			fprintf(OUT,"Case #%d: %d\n",t + 1, tot);
		}
	}
	fclose(in);
	fclose(OUT);
}