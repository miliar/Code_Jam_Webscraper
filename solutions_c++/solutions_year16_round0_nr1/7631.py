#include<stdio.h>
int main()
{
	int t,i,flag;
	FILE *ftp;
	long j,k,a[100],m,b[10];
	ftp=fopen("A-Small.out","w");
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		k=1;
		scanf("%d",&a[i]);
		b[0]=1;
		for(j=1;j<10;j++)
		b[j]=j;
		if(a[i]==0)
		{
			fprintf(ftp,"Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		m=a[i];
		while(1)
		{
			flag=1;
			k=a[i];
			while(k!=0)
			{
				if(k%10==0)
				b[0]=0;
			    for(j=1;j<10;j++)
			    {
				    if(b[j]==k%10)
				    {
					    b[j]=0;
					    break;
				    }
			    }
			    k/=10;
			}
			for(j=0;j<10;j++)
			if(b[j]!=0)
			flag=0;
			if(flag==1)
			{
				fprintf(ftp,"Case #%d: %d",i+1,a[i]);
				if(i!=99)
				fprintf(ftp,"\n");
				break;
			}
			else;
			a[i]+=m;
		}
	}
	fclose(ftp);
}
