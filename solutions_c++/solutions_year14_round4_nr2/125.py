#include<cstdio>
#include<algorithm>

int a[1000];
int b[1000];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		int i,j,k,n,min,res=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		i=0;j=n;
		while(i<j)
		{
			min=i;
			for(k=i;k<j;k++)if(a[k]<a[min])min=k;
			if(min-i<j-min-1)
			{
				res+=min-i;
				while(min>i)
				{
					a[min]=a[min-1];
					min--;
				}
				i++;
			}
			else
			{
				res+=j-min-1;
				while(++min<j)a[min-1]=a[min];
				j--;
			}
		}
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}