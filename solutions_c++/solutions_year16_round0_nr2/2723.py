#include <iostream>
#include <cstring>
using namespace std;

char s[110];

int flip(int pos) {
	char a[110]; int i;
	strcpy(a, s);
	for (i=0; i<=pos; i++) 
		if (a[pos-i]=='+') s[i] = '-'; else s[i] = '+';
	return 0;
}

int main() {
	int i,k,T;

	FILE *fin, *fout;
	fin = fopen("1.in", "r");
	fout = fopen("1.txt", "w");
	fscanf(fin, "%d", &T);
	for (k=0; k<T; k++) {
		fscanf(fin, "%s", s);
		fprintf(fout, "Case #%d: ",k+1);
		int t = strlen(s) - 1; int sum = 0;
		while (t>=0) {
			while ((t>=0)&&(s[t]=='+')) t--;
			if (t<0) break;
			if (s[0]=='-') flip(t); else {
				int h = 0;
				while ((s[h]=='+')&&(h<t)) h++;
				flip(h-1); flip(t); sum++;
				//fprintf(fout, "(%d %d %s %d)", h-1, t, s, sum);
			}
			sum++;
			//fprintf(fout, "(%s %d)", s, sum);
		}
		fprintf(fout, "%d\n", sum);
	}

	fclose(fin); fclose(fout);
	return 0;
}


