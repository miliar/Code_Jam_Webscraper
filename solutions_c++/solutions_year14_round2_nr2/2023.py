#include<stdio.h>
#include<stdlib.h>
int main()
{
	int T;scanf("%d",&T);
	for(int lT=1;lT <= T;lT++)
	{
		int a,b,k;
		scanf("%d %d %d",&a,&b,&k);
		int cnt = 0;
		for(int lx = 0;lx < a;lx++)
		{
			for(int ly = 0;ly < b;ly++){
				if((lx&ly) < k)
					cnt ++;
			}
		}
		printf("Case #%d: %d\n",lT,cnt);
	}
	return 0;
}
