#include <cstdio>
#include <algorithm>
using namespace std; 
int arr[6];
int p[101];
int main(void)
{
	freopen("C:\\Users\\user\\Desktop\\C-small-practice.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\out1.txt","w",stdout);

	int x;
	scanf("%d",&x);

    for(int i=1;i<=x;i++)
	{
		int num,q;
		scanf("%d%d",&num,&q);
		for(int j=0;j<q;j++)
		scanf("%d",&arr[j]);
		p[1]=1;
		p[num]=1;
		int min=1000000;
		
		do
		{
			int tot=0;
			for(int w=0;w<q;w++)
			{
				//printf("%d %d\n",arr[w],tot);
				p[arr[w]]=2;
				for(int m=arr[w]-1;m>=1;m--)
				{
					if(p[m]==1||p[m]==2)
					{
                       tot=tot+arr[w]-m;
					   //printf("%d\n",m);
					   if(p[m]==2)
					   tot=tot-1;
					   break;
					}
				}
				
				for(int m=arr[w]+1;m<=num;m++)
				{
					if(p[m]==1||p[m]==2)
					{
                       tot=tot+m-arr[w];
					   if(p[m]==2)
					   tot=tot-1;
					   //printf("%d\n",m);
					   break;
					}
				}
				//printf("%d %d\n",arr[w],tot);
			}
			
			if(min>tot)
			min=tot;
			memset(p,0,sizeof(p));
			p[1]=1;
			p[num]=1;
		}
		while(next_permutation(arr,arr+q));
		printf("Case #%d: %d\n",i,min);
		memset(p,0,sizeof(p));
	}
}