#include<stdio.h>
int main()
{ 
	FILE *fp=fopen("B-large.in","r");
	FILE *fp1=fopen("output.txt","w");
	int i,j,k,testcase,n,m,a[105][105],max,maxbyy[105],maxbyx[105],chk;
	fscanf(fp,"%d\n",&testcase);
	for(i=1;i<=testcase;i++)
	{
		chk=0;
		fscanf(fp,"%d %d\n",&n,&m);
		for(j=1;j<=n;j++)
		{
			max=0;
			for(k=1;k<=m;k++)
			{
				fscanf(fp,"%d ",&a[j][k]);
				if(max<a[j][k])
					max=a[j][k];
			}
			maxbyy[j]=max;
		}
		for(j=1;j<=m;j++)
		{
			max=0;
			for(k=1;k<=n;k++)
				if(max<a[k][j])
					max=a[k][j];
			maxbyx[j]=max;
		}
		for(j=1;j<=n;j++)
			for(k=1;k<=m;k++)
				if(a[j][k]<maxbyy[j] && a[j][k]<maxbyx[k] || a[j][k]>maxbyy[j] && a[j][k]>maxbyx[k])
					chk=1;
		if(chk==1)
			fprintf(fp1,"Case #%d: NO\n",i);
		else
			fprintf(fp1,"Case #%d: YES\n",i);
	}
	return 0;
}