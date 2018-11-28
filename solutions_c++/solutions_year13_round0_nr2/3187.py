#include <stdio.h>

int main(int argc , char * argv[])
{
	int T;
	scanf("%d",&T);
	for(int t = 0;t<T;t++)
	{
		int N,M;
		scanf("%d %d",&N,&M);
		//input
		int ** ar = new int * [N];
		for(int i = 0;i<N;i++)
		{
			ar[i] = new int [M];
		}

		for(int i = 0;i<N;i++)
		{
			for(int f = 0;f<M;f++)
			{
				scanf("%d",&ar[i][f]);
			}
		}
		//prc
		bool can = true;
		for(int i = 0;i<N;i++)
		{
			for(int j = 0;j<M;j++)
			{
				bool atrow = true;
				bool atcol = true;
				for(int k = 0;k<N;k++)
				{
					if(ar[i][j] < ar[k][j])
					{
						atcol = false;
					}
				}
				for(int l = 0;l<M;l++)
				{
					if(ar[i][j] < ar[i][l])
					{
						atrow = false;
					}
				}
				if(atrow == false && atcol == false)
				{
					can = false;
				}
			}
		}
		if(can == true)
		{
			printf("Case #%d: YES\n",(t+1));
		}
		if(can == false)
		{
			printf("Case #%d: NO\n",(t+1));
		}

	}

	return 0;
}