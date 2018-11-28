#include<stdio.h>

int main()
{
	int t,n,i,j,ans,count,tmp;
	char ch;
	FILE *fp,*fp1;
	if((fp = fopen("A-large.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("a-large-output.in","w");
	fscanf(fp,"%d",&t);
	for(i = 1;i <= t;i++){
		ans = 0;
		ch =  fgetc(fp);
		fscanf(fp,"%d",&n);
		ch =  fgetc(fp);
		char a[n+2];
		fscanf(fp,"%c",&a[0]);
		count = a[0] - 48;
		for(j = 1;j <= n;j++) {
			fscanf(fp,"%c",&a[j]);
			if(count >= j) {
				count += a[j] - 48;
			} else {
				tmp = a[j] - 48;
				if(tmp != 0) {
					ans += j - count;
					count = count + j - count + a[j] - 48;
				}		
			}
		}
		fprintf(fp1,"Case #%d: %d\n",i,ans);
	}
	return 0;
}
