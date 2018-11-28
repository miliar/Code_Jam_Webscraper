#include <stdio.h>
#include <stdlib.h>
struct playerthing {
	double score;
	int from;
};

int comparept (const void * a, const void * b) {
	playerthing* x = (playerthing*) a;
	playerthing* y = (playerthing*) b;
	return (x->score-y->score)>0?1:-1;
}

int main() {
	int casenum=0;
	FILE *fp = fopen("in","r");
	fscanf(fp, "%d",&casenum);
	playerthing *p;
	p = new playerthing[10000];
	for (int casei=1;casei<=casenum;casei++) {
		int num;
		fscanf(fp,"%d",&num);
		for (int i=0;i<2*num;i++) {
			fscanf(fp,"%lf",&(p[i].score));
			if (i<num) p[i].from=1;
			else p[i].from=2;
		}
		qsort(p,2*num,sizeof(playerthing),comparept);
		int backr1=0,r1=0;
		int backr2=0,r2=0;
		for (int i=0;i<2*num;i++) {
			if (p[i].from==1) {
				if (backr2>0) backr2--;
				else r1++;
				backr1++;
			}
			if (p[i].from==2) {
				if (backr1>0) backr1--;
				else r2++;
				backr2++;
			}
		}
		fprintf(stdout,"Case #%d: %d %d\n", casei, num-r1, r2);
	}
	return 0;
}
