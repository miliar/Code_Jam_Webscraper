#include<stdio.h>
int main()
{
	int T,o;
	scanf("%d",&T);
	for(o=1;o<=T;o++)
	{
		int r,t,cnt;
		scanf("%d %d",&r,&t);
		for(cnt=0;t>=0;)
		{
			if(t-((2*r)+1)>=0)
			{
				t-=((2*r)+1);
				cnt+=1;
				r+=2;
			}
			else
				break;
		}
		printf("Case #%d: %d\n",o,cnt);
	}
}