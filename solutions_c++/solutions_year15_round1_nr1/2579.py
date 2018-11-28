#include<iostream>
#include<string>

int main()
{
	int T;
	int N;
	int m[1000];
	int diffm[999];
	int y,z,diffmax;
	scanf("%d",&T);
	for(int i=0; i<T; i++)
	{
		scanf("%d",&N);
		diffmax = 0;
		for(int j=0; j<N; j++)
		{
			scanf("%d",&m[j]);
			if(j != 0)
			{
				diffm[j-1] = m[j-1] - m[j];
				if(diffmax < diffm[j-1])
					diffmax = diffm[j-1];
			}
		}
		y=0;
		z=0;
		for(int j=0; j<N-1; j++)
		{
			if(diffm[j] <= 0)
			{
				y+=0;
				z+=diffmax>=m[j]?m[j]:diffmax;
			}
			else
			{
				y+=diffm[j];
				z+=diffmax>=m[j]?m[j]:diffmax;
			}
		}
		
		printf("Case #%d: %d %d\n",(i+1),y,z);
	}
	return 0;
}