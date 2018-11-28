#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *ftp;
	ftp=fopen("aaa.txt","w");
	int T,i;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		int n,j,k,l;
		scanf("%d",&n);
		int a[n],sum=0,aa;
		for(j=0;j<n;j++)
		{
		scanf("%d",&a[j]);
		sum+=a[j];
		}
		fprintf(ftp,"Case #%d: ",i+1);
		while(sum!=0)
		{
			int aa=0,bb=0,cc,dd;
			for(k=0;k<n;k++)
			{
				if(aa<=a[k])
				{
					aa=a[k];
					cc=k;
				}
			}
			
			for(k=0;k<n;k++)
			{
				if(bb<=a[k]&&k!=cc)
				{
					bb=a[k];
					dd=k;
				}
			}//printf("   %d %d  ",cc,dd);
			if(aa==1&&bb==1&&sum==3)
			{
				fprintf(ftp,"%c ",cc+65);
				a[cc]--;
				sum--;
				continue;
			}
			else
			{
				a[cc]--;
				a[dd]--;
				sum-=2;
				if(sum!=0)
				fprintf(ftp,"%c%c ",cc+65,dd+65);
				else
				fprintf(ftp,"%c%c\n",cc+65,dd+65);
				continue;
			}
		}
	}
	fclose(ftp);
}
