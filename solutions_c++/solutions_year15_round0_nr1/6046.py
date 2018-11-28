#include<stdio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
	int t,size,n,count,k,i,j=1;
	char a[1001];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&size);
		scanf("%s",&a);
		count=int(a[0])-48;
		n=0;
		for(k=1;k<size+1;k++)
		{
			for(i=1;i<=int(a[k])-48;i++)
		    {
		    	if(k<=count)
		    	count++;
		    	else
		    	{
		    		n=n+k-count;
		    		count=count+(k-count)+1;
				}
			}
		}
		printf("Case #%d: %d\n",j,n);
		j++;
	}
return 0;
}

