#include <stdio.h>
#define f(i,n) for(int i =0; i<n;i++)
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	f(i,t)
	{
		int b,c;
		scanf("%d",&b);
		int bo[16];
		f(j,16)
			scanf("%d", bo+j);
		scanf("%d",&c);
		int bo2[16];
		f(j,16)
			scanf("%d", bo2+j);
		int same=0;
		int ans = 0;
		for(int k = (c-1)*4;k<c*4;k++)
			for(int j=(b-1)*4;j<b*4;j++)
				if(bo[j]==bo2[k])
				{
					//printf("%d %d %d %d\n",k,j, c, b);
					same++;
					ans=bo[j];
				}
		if(same==1)
			printf("Case #%d: %d\n",i+1,ans);
		else if(same==0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else
			printf("Case #%d: Bad magician!\n",i+1);
	}		
}
