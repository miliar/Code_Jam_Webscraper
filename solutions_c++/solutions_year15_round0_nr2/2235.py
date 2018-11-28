#include <stdio.h>

using namespace std;

int x[1010];

int main()
{
	int i,j,k,q,n,min,max,cnt,chk;	
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	scanf("%d",&q);
	for(k=1;k<=q;k++)
	{
		min=1<<30,max=0;
		printf("Case #%d: ",k);
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&x[i]);
			if(x[i] > max) max=x[i];
		}
		for(j=1;j<=max;j++)
		{
			cnt=0,chk=0;
			for(i=0;i<n;i++)
			{
				if(x[i]<=j) continue;
				if(x[i]%j) cnt+=(x[i]/j),chk=1;
				else cnt+=(x[i]/j)-1;
			}
			cnt+=j;
			// printf("\nj=%d cnt=%d",j,cnt);
			if(min>cnt) min=cnt;
		}
		printf("%d\n",min);
	}
	return 0;
}