#include <stdio.h>
int main() {
	FILE *fp = fopen("A-small-attempt2.in","r");
	FILE *fpw = fopen("output.txt", "w");
	int T, sm;
	fscanf(fp, "%d", &T);
	for (int i=0; i<T; i++) {
		fscanf(fp,"%d", &sm);
		char str[sm+1];
		fscanf(fp, "%s", str);
		int total=0, add=0, tmp;
		total = (int) str[0]-'0';
		for (int j=1; j<sm+1; j++) {
			tmp = (int) str[j]-'0';
			if (tmp>0) {
				if (total<j) {
					add += (j-total);
					total+=add;
				}
				total+=tmp;
			}
		}
		fprintf(fpw,"Case #%d: %d\n",i+1,add);
	}
}
