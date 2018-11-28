#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main () {

	char s[1001],r[1001]={'\0'},aux;
	FILE *in;
	FILE *out;
	int t,n;
	in = fopen ("A-large.in","r");
	out = fopen ("Al.out","w");

	fscanf(in,"%d",&t);
	const int T=t;

	for (int i=0;i<T;i++) {
		fscanf (in," %s",&s);
		n=strlen(s);
		r[1]=r[0];
		r[0]=s[0];
		for (int j=1;j<n;j++) {
			if (s[j]>=r[0]) {
				for (int k=0;k<=j;k++) {
					r[j-k+1]=r[j-k];
				}
				r[0]=s[j];
			}
			else {
				r[j+1]=r[j];
				r[j]=s[j];
			}
		}
		if (i==(T-1)) fprintf(out,"Case #%d: %s",i+1,r);
		else fprintf(out,"Case #%d: %s\n",i+1,r);
		r[0]='\0';
	}

	fclose(in);
	fclose (out);
	return 0;
}