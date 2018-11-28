#include <stdio.h>
int main() {
	int casenum=0;
	FILE *fp = fopen("in","r");
	fscanf(fp, "%d",&casenum);
	int bbb[8];
	for (int casei=1;casei<=casenum;casei++) {
		int ln=0, p=0;
		int x=0;
		fscanf(fp,"%d",&ln);
		ln--;
		for (int j=0;j<ln;j++) fscanf(fp,"%d %d %d %d",&x,&x,&x,&x);
		fscanf(fp,"%d %d %d %d",bbb+(p++),bbb+(p++),bbb+(p++),bbb+(p++));
		for (int j=ln+1;j<4;j++) fscanf(fp,"%d %d %d %d",&x,&x,&x,&x);

        fscanf(fp,"%d",&ln);
        ln--;
        for (int j=0;j<ln;j++) fscanf(fp,"%d %d %d %d",&x,&x,&x,&x);
        fscanf(fp,"%d %d %d %d",bbb+(p++),bbb+(p++),bbb+(p++),bbb+(p++));
        for (int j=ln+1;j<4;j++) fscanf(fp,"%d %d %d %d",&x,&x,&x,&x);

		int count[17] = {0};
		for (int j=0;j<8;j++) {
			count[bbb[j]]++;
		}
		int finalr=0;
		int num2=0;
		for (int j=1;j<=16;j++) {
			if (count[j]==2) {
				num2++;
				finalr=j;
			}
		}
		if (num2==1) {
			fprintf(stdout,"Case #%d: %d\n", casei, finalr);
		}
		if (num2==0) {
			fprintf(stdout,"Case #%d: Volunteer cheated!\n", casei);
		}
		if (num2>1) {
			fprintf(stdout,"Case #%d: Bad magician!\n", casei);
		}   
	}
	return 0;
}
