#include <cstdio>
#include <cstring>
int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int T;
	char S[1001];
	char P[2001];
	scanf("%d\n", &T);
	for (int i = 1; i <= T; i++){
		gets(S);
		int len = strlen(S);
		int l_pointer = 1000;
		int r_pointer = 1000;
		for (int j = 0; j < len; j++){
			if (j == 0){
				P[r_pointer] = S[j];
				r_pointer++;
			} else if (S[j] >= P[l_pointer]){
				l_pointer--;
				P[l_pointer] = S[j];
			} else {
				P[r_pointer] = S[j];
				r_pointer++;
			}
		}
		printf("Case #%d: ", i);
		for (int j = l_pointer; j < r_pointer; j++)
			printf("%c", P[j]);
		printf("\n");
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
