#include<stdio.h>

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, P[1500], D;
	scanf("%d",&T);
	for(int c=1;c<=T;c++)
	{
		scanf("%d",&D);
		int max=-1;
		int ans=2000;
		for(int i=0;i<D;i++)
		{
			scanf("%d",&P[i]);
			max = P[i]>max?P[i]:max;
		}

		for(int make = 1; make<=max; make++)
		{
			int minutes = 0;
			for(int i=0;i<D;i++)
			{
				if(P[i] > make)
					minutes += ((P[i]-1)/make);
			}
			int ansmake = minutes + make;
			ans = ansmake<ans ? ansmake:ans;
		}
		printf("Case #%d: %d\n",c, ans);
	}
}