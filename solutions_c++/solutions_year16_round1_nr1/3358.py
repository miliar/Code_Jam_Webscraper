#include <cstdio>
#include <cstring>
#include<iostream>
#include<ctime>  
#include<algorithm>
#include<ext/hash_map>
using namespace std;

int main() {
	FILE *fp, *fp2;
	fp = fopen("A-large.in", "r");
	fp2 = fopen("A-large.out", "w");
	int T, Tpie, N;
	char s[1005];
	char q[1005];
	fscanf(fp, "%d\n", &T);
	Tpie = T;
	while (Tpie--) {
		fscanf(fp, "%s\n", s);
		int len = strlen(s);
		for (int i = 0; i < 1005; i++)
			q[i] = '\0';
		q[0] = s[0];
		for (int i = 1; i < len; i++) {
			if (s[i] >= q[0]) {
				for (int j = i; j >= 1; j--)
					q[j] = q[j - 1];
				q[i + 1] = '\0';
				q[0] = s[i];
			}
			else {
				q[i + 1] = '\0';
				q[i] = s[i];
			}
		}
		fprintf(fp2, "Case #%d: %s\n", T - Tpie, q);
		
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}