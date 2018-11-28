#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		int ans = 0, s, sm = 0, k;
		char str[1010] ={0};
		scanf("%d %s\n", &s, &str);
		if (s > 0)
		{
			sm = (int)(str[0] - '0');
			for(int i = 1; i <= s ; i++)
			{
				k = (int)(str[i] - '0');
				if(sm < i)
				{
					ans += i - sm;
					sm = i;
				}
				sm += k;
			}
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}