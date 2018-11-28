#include <stdio.h>

int main(int argc, char const *argv[])
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.txt","w",stdout);
	int T,cass=1;
	scanf("%d",&T);
	while(T--)
	{
		int t,r,count=0;
		scanf("%d %d",&r,&t);
		int num=(r+1)*(r+1)-r*r;
		while(t>=num)
		{
			t=t-num;
			r+=2;
			num=(r+1)*(r+1)-r*r;
			count++;
		}
		printf("Case #%d: %d\n",cass++,count);
	}
	return 0;
}
