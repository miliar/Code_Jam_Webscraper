#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
bool rem[11];
int main()
{
//	freopen("A-large.in", "r", stdin);
	//freopen("in.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int n;
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		int flag = 0, p; 
		long long tmp = 0ll, ans = 0ll;
		for (int i = 1; i <= 10; i++)
			rem[i - 1] = 0;
		for (int i = 1; (i <= 10000000&&flag != 10); i++)
		{
			ans += n, tmp = ans;
			while(tmp)
			{
				p = tmp % 10;
				if(!rem[p]) rem[p] = 1, flag++;
				tmp /= 10;
			}
			//printf("%d %d\n", i, flag);
			//printf("ok\n");
		}
		if(flag == 10) printf("Case #%d: %lld\n", t, ans);
		else printf("Case #%d: INSOMNIA\n", t); 
	} 
	return 0;
} 
