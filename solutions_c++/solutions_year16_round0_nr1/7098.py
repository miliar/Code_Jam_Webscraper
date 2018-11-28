#include <cstdio>
#include <cstring>
using namespace std;

int main(void)
{
	int cases;
	scanf("%d",&cases);
	for (int ca=1;ca<=cases;ca++)
	{
		int n;
		long long t;
		scanf("%d",&n);
		
		printf("Case #%d: ",ca);
		if (n==0)
			printf("INSOMNIA\n");
		else
		{
			int digit[10];
			int cnt;
			cnt=10;
			memset(digit,0,sizeof(digit));
			for (int i=1;;i++)
			{
				t=i*n;
				while (t>0)
				{
					if (!digit[t%10])
					{
						cnt--;
						digit[t%10]=1;
					}
					
					t=t/10;
					
					if (!cnt)
						break;
				}
				if (!cnt)
				{
					t=n*i;
					break;
				}
			}
			
			printf("%lld\n",t);
		}
	}
	return 0;
}
