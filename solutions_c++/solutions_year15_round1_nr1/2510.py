#include<stdio.h>

int main()
{
	int t,i,j,n,min1,min2,d,dm;
	char ch;
	FILE *fp,*fp1;
	if((fp = fopen("A-large.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("a-large-output.in","w");
	fscanf(fp,"%d",&t);
	for(i = 1;i <= t;i++){
		ch =  fgetc(fp);
		fscanf(fp,"%d",&n);
		ch =  fgetc(fp);
		min1 = 0;
		min2 = 0;
		dm = 0;
		int a[n];
		fscanf(fp,"%d",&a[0]);
		for(j = 1;j < n;j++) {
			fscanf(fp,"%d",&a[j]);
			d = a[j-1] - a[j];
			if(d > dm) dm = d;
			if(d > 0) min1 += d;
		}
		n--;
		for(j = 0;j < n;j++) {
			if(a[j] > dm) min2 += dm; 
			else min2 += a[j];
		}
		fprintf(fp1,"Case #%d: %d %d\n",i,min1,min2);
	}
	fclose(fp);
	return 0;
}
