#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int t, ys, n;
char str[5010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("dataA-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d%s",&n,str);
		int ans = 0, sum = 0;
		for (int i=0;i<=n;++i)
		{
			int temp = max(0, i - sum);
			ans += temp;
			sum += temp;
			sum += str[i] - '0';
		}

		printf("Case #%d: %d\n", ++ys, ans);
	}


	return 0;
}