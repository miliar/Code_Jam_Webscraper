#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int c=0;c<t;c++)
	{
		long long int n;
		scanf("%lld",&n);

		int x = 10;
		int A[10];
		memset(A,0,sizeof(A));
		long long int y = n;

		if(n)
		{
			while(x)
			{
				long long int p = y;

				while(p)
				{
					if(A[p%10] == 0)
					{
						A[p%10] = 1;
						x--;
					}

					p /= 10;
				}

				if(x)
					y += n;
			}

			printf("Case #%d: %lld\n",c+1,y);
		}
		else
			printf("Case #%d: INSOMNIA\n",c+1);
			
	}
}