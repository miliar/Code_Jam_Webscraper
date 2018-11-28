#include<stdio.h>

int main()
{
	int t,i,j,a[10],sum,k,N;
	long long int n,ans,tmp;
	FILE *fp,*fp1;
	if((fp = fopen("A-large.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("a-large-output.in","w");
	fscanf(fp,"%d",&t);
	for(i = 1;i <= t;i++){
		ans = 0;
		for(j=0;j<10;j++) a[j] = 1;
		fscanf(fp,"%d",&N);
		if(N==0) {
			fprintf(fp1,"Case #%d: INSOMNIA\n",i);
			continue;
		} 
		n=0;
		while(1) {
			tmp = n+N;
			n=tmp;
			while(tmp != 0) {
				a[tmp%10] = 0;
				tmp=tmp/10;
			}
			sum=0;
			for(k=0;k<10;k++) sum=sum+a[k];
			if(sum==0) break;
		}
		ans=n;
		fprintf(fp1,"Case #%d: %lld\n",i,ans);
	}
	fclose(fp);
	return 0;
}
