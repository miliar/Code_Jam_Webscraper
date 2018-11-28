#pragma warning(disable:4996)
#include<fstream>
#define N 2002

using namespace std;

int T, alpha[32], n, topolgy[20] = {8,3,0,4,2,6,1,5,7,9};
char s[N],key[30];
char num[11][6] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int nn[11] = { 4,3,3,5,4,4,3,5,5,4 };
int sol[N];
void solve();
void pre_processing();
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i,j,k;
	pre_processing();
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		for (j = 0; j < 30; j++) sol[j] = 0;
		solve();
		printf("Case #%d: ", i + 1);
		for (j = 0; j < 10; j++) {
			for (k = 0; k < sol[j]; k++) printf("%d", j);
		}
		printf("\n");
	}
	return 0;
}

void pre_processing()
{
	key[8] = 'G';
	key[3] = 'G';
	key[0] = 'Z';
	key[2] = 'W';
	key[6] = 'X';
	key[4] = 'R';
	key[1] = 'O';
	key[5] = 'F';
	key[7] = 'V';
	key[9] = 'N';
}

void solve()
{
	int i,j,k,p=0,min;
	scanf("%s", s);
	n = strlen(s);
	for (i = 0; i < 30; i++) alpha[i] = 0;
	for (i = 0; i < n; i++) alpha[s[i] - 'A']++;
	
	for (i = 0; i < 10; i++) {
		k = topolgy[i]; min = 5000;
		for (j = 0; j < nn[k]; j++) {
			if (alpha[num[k][j]-'A'] < min) min = alpha[num[k][j] - 'A'];
		}
		sol[k] = min;
		for (j = 0; j < nn[k]; j++) {
			alpha[num[k][j] - 'A']-=min;
		}
	}

}