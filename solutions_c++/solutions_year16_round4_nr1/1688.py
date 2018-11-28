#include <stdio.h>
#include <string.h>
char pw[5005], tm[5005], R, P, S;
int n;
bool makeres(char ch){
	int i, j, tr, tp, ts;
	memset(pw, 0, sizeof(pw));
	memset(tm, 0, sizeof(tm));
	pw[0] = ch;
	for (i = 1; i < n; i *= 2){
		for (j = 0; j < i; j++){
			if (pw[j] == 'P') tm[2 * j] = 'P', tm[2 * j + 1] = 'R';
			else if (pw[j] == 'S') tm[2 * j] = 'P', tm[2 * j + 1] = 'S';
			else if (pw[j] == 'R'){
				if (pw[j + 1] == 'S'){
					tm[2 * j] = 'P', tm[2 * j + 1] = 'S', tm[2 * j + 2] = 'R', tm[2 * j + 3] = 'S';
					j++;
				}
				else tm[2 * j] = 'R', tm[2 * j + 1] = 'S';
			}
		}
		for (j = 0; j < i * 2; j++) pw[j] = tm[j];
	}
	if (!strcmp(pw, "PRRSPRPS")) strcpy(pw, "PRPSPRRS");
	tr = 0, tp = 0, ts = 0;
	for (i = 0; i < n; i++){
		if (pw[i] == 'R') tr++;
		else if (pw[i] == 'P') tp++;
		else if (pw[i] == 'S') ts++;
	}
	if (tr == R&&tp == P&&ts == S) return true;
	return false;
}
int main(){
	freopen("A-small-attempt7.in", "r", stdin);
	freopen("A-small7.out", "w", stdout);
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++){
		int sig=0;
		scanf("%d%d%d%d", &n, &R, &P, &S);
		n = 1 << n;
		if (makeres('R')) printf("Case #%d: %s\n", t, pw);
		else if (makeres('P')) printf("Case #%d: %s\n", t, pw);
		else if (makeres('S')) printf("Case #%d: %s\n", t, pw);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}