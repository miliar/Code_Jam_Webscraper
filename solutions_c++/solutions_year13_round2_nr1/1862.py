#include <cstdio>
#include <vector>
#include <algorithm>


using namespace std;

int size,t,n,x;
vector<int> V;

int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		scanf("%d %d", &size, &n);
		for (int j = 0; j < n; ++j)
		{
			scanf("%d", &x);
			V.push_back(x);
		}
		sort(V.begin(), V.end());
		
		int j = 0, cur=0, pre=size, act=0,tmp=0;

		while(j<n)
		{
			if(size==1)
			{
				cur=n;
				break;
			}

			if(V[j] >= size)
			{
				/*if(size*2 <= V[j]-1)
				{
					cur+=n-j;
					break;
				}
				else
				{
					size+=size-1;
					cur++;
				}*/
				act=0;
				while(size<=V[j])
				{
					size+=size-1;
					act++;
				}
				
				if(act>=n-j)
				{
					cur+=n-j;
					break;
				}
				else
					cur+=act;
			}

			if(cur==0)
				tmp++;
			
			size+=V[j];		
			j++;
		}

		printf("Case #%d: %d\n", i+1, min(n-tmp,cur), pre, n);
		/*for (int i = 0; i < n; ++i)
			printf("%d ", V[i]);
		
		printf("\n");*/
		V.clear();
	}

	return 0;
}