#include <stdio.h>

int ans1 = 0;
int ans2 = 0;
int fst[6][6] = {0};
int snd[6][6] = {0};
FILE *fin;
FILE *fout;

void input(void)
{
	int i, j;
	fscanf(fin, "%d", &ans1);
	for (i=1;i<=4;++i){
		for (j=1;j<=4;++j){
			fscanf(fin, "%d", &fst[i][j]);
		}
	}
	fscanf(fin, "%d", &ans2);
	for (i=1;i<=4;++i){
		for (j=1;j<=4;++j){
			fscanf(fin, "%d", &snd[i][j]);
		}
	}
}

int proc(void)
{
	int chk[18]={0};
	int i;
	for (i=1;i<=4;++i){
		chk[fst[ans1][i]]++;
	}
	for (i=1;i<=4;++i){
		chk[snd[ans2][i]]++;
	}
	int res = -1;
	for (i=1;i<=16;++i){
		if (chk[i] == 2){
			if (res == -1) res = i;
			else return -1;
		}
	}
	if (res == -1) return -2;
	else return res;
}

void output(int t, int ans)
{
	fprintf(fout, "Case #%d: ", t);
	if (ans == -1) {
		fprintf(fout, "Bad magician!");
	} else if (ans == -2) {
		fprintf(fout, "Volunteer cheated!");
	} else {
		fprintf(fout, "%d", ans);
	}
	fprintf(fout, "\n");
}
int main(void)
{
	int T;
	int t;
	int ans;
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (t=1;t<=T;++t){
		input();
		ans = proc();
		output(t, ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
