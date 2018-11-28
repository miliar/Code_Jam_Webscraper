#include<stdio.h>
int main()
{
	FILE *ftp;
	ftp=fopen("aaa.txt","w");
	int T,i,j,k,m,n;
	char a[102][1002];
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		char b[2004];
		scanf("%s",a[i]);
		b[1002]=a[i][0];
		m=1002;
		n=1002;
		for(j=1;a[i][j]!='\0';j++)
		{
			if(a[i][j]<b[m])
			{
				b[n+1]=a[i][j];
				n++;
			}
			else
			{
				b[m-1]=a[i][j];
				m--;
			}
		}
		fprintf(ftp,"Case #%d: ",i+1);
		for(j=m;j<=n;j++)
		fprintf(ftp,"%c",b[j]);
		fprintf(ftp,"\n");
	}
	fclose(ftp);
}
