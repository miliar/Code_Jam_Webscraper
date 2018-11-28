#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T,N;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		bool flags[10]={false};
		int R=0;
		scanf("%d",&N);
		if(N==0)
		{
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		while(!(flags[0]&&flags[1]&&flags[2]&&flags[3]&&flags[4]&&flags[5]&&flags[6]&&flags[7]&&flags[8]&&flags[9]))
		{
			int factor=1;
			R+=N;
			while(R/factor>0)
			{
				flags[(R/factor)%10]=true;
				factor*=10;
			}
		}
		printf("Case #%d: %d\n",i+1,R);
	}
	return 0;
}