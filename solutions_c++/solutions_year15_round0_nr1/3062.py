#include "cstdio"
#include "cstring"
#include "cmath"
#include "algorithm"

using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int test=1;test<=t;test++)
	{
		int n;
		scanf("%d", &n);
		char inputs[n+2];
		scanf("%s", inputs);

		int ans = 0;
		int now = 0;

		for(int i=0;i<=n;i++)
		{
			ans += max(0, i-now);
			now = max(now, i);
			now += inputs[i]-'0';			
		}

		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
