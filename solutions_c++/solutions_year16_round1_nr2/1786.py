#include<stdio.h>
#include<stdlib.h>
int cmp(const void *a,const void*b)
 {
 return(*(char *)a-*(char*)b);
}
int main()
{
	FILE *ftp;
	ftp=fopen("bbb.txt","w");
	int T,n,i,j,k,l;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		int a[2600][2]={0},b[52]={0},t=0,p=0,flag=0,nn=0,temp;
		scanf("%d",&n);
		for(j=0;j<2*n-1;j++)
		{
			for(k=0;k<n;k++)
			{
				flag=0;
				scanf("%d",&t);
				for(l=0;l<=p;l++)
				{
					if(a[l][0]==t)
					{
						a[l][1]++;
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					a[p+1][0]=t;
					a[p+1][1]=1;
					p++;
				}
			}
		}
		for(j=0;j<=p;j++)
		{
			if(a[j][1]%2==1)
			{
				b[nn]=a[j][0];
				nn++;
			}
		}
		for (j = 0; j < n-1 ; j++)
        for (k = 0; k < n -1- j; k++)
        {
            if(b[k] > b[k + 1])
            {
                temp = b[k];
                b[k] = b[k + 1];
                b[k + 1] = temp;
            }
        }

		fprintf(ftp,"Case #%d: ",i+1);
		for(j=0;j<n-1;j++)
		fprintf(ftp,"%d ",b[j]);
		fprintf(ftp,"%d\n",b[n-1]);
	}
}
