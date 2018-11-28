#include<stdio.h>
#include<string.h>
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");
#define Limit 2000

int Visit[30],len,A_cnt=0,Sum;
char S[100],Answer[30];

char D[10][10] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};


int check(int x, int k) {
	int i, j,ch_len =strlen(D[x]),flag=0;
	for (i = 0; i < ch_len; i++) {
		Visit[D[x][i] - 'A'] -= k;
		Sum -= k;
		if (Visit[D[x][i] - 'A']<0)flag = 1;
	}

	return flag;
}
int dfs(int x, int k) {
	if (Sum == 0) {
		return 0;
	}

	int i;
	for (i = 0; i < 10; i++) {
		if (check(i, 1) == 0) {
			Answer[A_cnt++] = i + '0';
			dfs(0, i);
			if (Sum == 0) break;
			Answer[--A_cnt] = 0;
		}
		check(i, -1);

	}

	return 0;
}

int A()
{
	int i;
	A_cnt = 0; Sum = 0;
	for (i = 0; i < 30; i++) {
		S[i] = 0;
		Visit[i] = 0;
		Answer[i] = 0;
	}

	fscanf(in,"%s", S); 
	len = strlen(S); Sum = len;
	for (i = 0; i < len; i++) {
		Visit[S[i]-'A']++;
	}

	for (i = 0; i < 10; i++) {
		if (check(i, 1) == 0) {
			Answer[A_cnt++] = i+'0';
			dfs(0, i);
			if (Sum == 0) break;
			Answer[--A_cnt] = 0;
		}
		check(i, -1);

	}

	fprintf(out, "%s\n",Answer);
	return 0;
}


int main()
{
	int T,i=1; fscanf(in,"%d",&T);

	while (T--) {
		fprintf(out,"Case #%d: ",i++);
		A();
	}

	return 0;
}