#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		int N;
		scanf("%d",&N);
		
		printf("Case #%d: ",t);
		
		if (N)
		{
			int used[10] = { 0 };
			int cc = 0;
			for (int i = 1; i <= 1000; i += 1)
			{
				int n = i*N;
				while (n)
				{
					int d = n%10;
					n /= 10;
					
					if (!used[d])
					{
						used[d] = true;
						++cc;
					}
				}
				
				if (cc == 10)
				{
					N = i*N;
					break;
				}
			}
			
			printf("%d\n",N);
		}
		else
			printf("INSOMNIA\n");
	}
	return 0;
}
