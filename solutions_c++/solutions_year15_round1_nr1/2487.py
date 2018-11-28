#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	int T,c=1;
	scanf("%d",&T);
	while(T--)
	{
		int N;
		scanf("%d",&N);
		int y=0,z=0,min = 0;
		vector<int> M;
		for(int i=0;i<N;i++)
		{
			int p;
			scanf("%d",&p);
			M.push_back(p);
		}
		for(int i=1;i<M.size();i++)
		{
			int v = M[i-1] - M[i];

			if(v > 0 && v > min)
			{
				min = v;
			}

			if(v > 0)
			{
				y+=v;
			}
		}
		for(int i=1;i<M.size();i++)
		{
			int v = M[i-1] - M[i];

			if(v < min )
			{
				if(M[i-1] < min)
				{
					z+=M[i-1];
				}
				else
				{
					z+=min;
				}
			}
			else
			{
				if(M[i-1] <= min)
				{
					z+=M[i-1];
				}
				else
				{
					z+=min;
				}
			}
		}
		printf("Case #%d: %d %d\n",c++,y,z);
	}
	return 0;
}