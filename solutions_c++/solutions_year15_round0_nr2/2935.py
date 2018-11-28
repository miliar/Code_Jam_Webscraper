#include "cstdio"
#include "cstring"
#include "algorithm"

using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int test = 1;test<=t;test++)
	{
		int ans = 1000000000;

		int mx = -1;

		int n, in[1002];
		scanf("%d", &n);

		for(int i=0;i<n;i++)
		{
			scanf("%d", &in[i]);
			mx = max(mx, in[i]);			
		}

		for(int i = 1;i<=mx;i++) {
			int buff = i;
			for(int j=0;j<n;j++)
			{
				int div = in[j]/i - (in[j] % i == 0);
				buff += div;
			}
			ans = min(ans, buff);		
		}

		printf("Case #%d: %d\n", test, ans);	
	}

	return 0;
}

