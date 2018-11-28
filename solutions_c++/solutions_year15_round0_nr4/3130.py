#include<stdio.h>

int main()
{
	int t,i,x,r,c,tmp;
	bool found;
	char ch;
	FILE *fp,*fp1;
	if((fp = fopen("D-small-attempt0.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("d-small-output.in","w");
	fscanf(fp,"%d",&t);
	ch=fgetc(fp);
	for(i = 1;i <= t;i++) {
		found = true;
		fscanf(fp,"%d",&x);
		ch = fgetc(fp);
		fscanf(fp,"%d",&r);
		ch = fgetc(fp);
		fscanf(fp,"%d",&c);
		ch = fgetc(fp);
		if(x == 1) {
			fprintf(fp1,"Case #%d: GABRIEL\n",i);
			continue;
		} 
		if(x >= 7) {
			fprintf(fp1,"Case #%d: RICHARD\n",i);
			continue;
		}
		tmp = r*c;
		if(tmp < x) {
			fprintf(fp1,"Case #%d: RICHARD\n",i);
			continue;
		}
		tmp = tmp % x;
		if(tmp != 0) {
			fprintf(fp1,"Case #%d: RICHARD\n",i);
			continue;
		}
		if(x == 2) {
			fprintf(fp1,"Case #%d: GABRIEL\n",i);
			continue;
		}
		if(r >= x) {
			tmp = x/2 + 1;
			if(c >= tmp) {
				fprintf(fp1,"Case #%d: GABRIEL\n",i);
				continue;
			} else {
				fprintf(fp1,"Case #%d: RICHARD\n",i);
				continue;
			}
		} else if(c >= x) {
			tmp = x/2 + 1;
			if(r >= tmp) {
				fprintf(fp1,"Case #%d: GABRIEL\n",i);
				continue;
			} else {
				fprintf(fp1,"Case #%d: RICHARD\n",i);
				continue;
			}	
		} else {
			fprintf(fp1,"Case #%d: RICHARD\n",i);
			continue;
		}
	}
	fclose(fp);
	return 0;
}
