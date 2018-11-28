#include<stdio.h>
int main()
{
	int t,x;
	scanf("%d",&t);
	for(x=1;x<=t;x++)
	{
		long int n,i,j,a[10],r,k=0;
		FILE *fptr;
        fptr=fopen("output.txt","a");
		scanf("%ld",&n);
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		if(n==0)
		{
				fprintf(fptr,"Case #%d: INSOMNIA\n",x);
				continue;
		}
		i=1;
		while(1)
		{
			j=i*n;
		    while(j!=0)
		    {
			r=j%10;
			if(a[r]==0)
			{
			k++;
			a[r]=1;
		    }
			j=j/10;
		    }
		    if(k==10)
		    break;
		    i++;
		}
		fprintf(fptr,"Case #%d: %ld\n",x,n*i);
		k=0;
	}

return 0;	
}
