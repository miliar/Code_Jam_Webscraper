#include <cstdio>
using namespace std;

int T,t;
int n;
long sum;
int m,Max;
int a[1001];
int ansmin = 10001;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d", &T);
	t = 1;
	while(T--)
	{
			scanf("%d", &n);
			sum = 0;
			Max = 0;
			ansmin = 10001;
			int k;
			for(int i = 1; i <= n;i++)
			{
				scanf("%d", &a[i]);
			
				if(a[i] > Max)Max = a[i];
			}

			for(m = 1; m <= Max; m++)
			{
				sum = 0;
				for(k = 1; k <= n; k++)
				{
					sum += (a[k] - 1)/m;
				}
				if(sum + m < ansmin)ansmin = sum + m;
			}

			printf("Case #%d: %d\n",t++,ansmin);
	}
	return 0;
}
