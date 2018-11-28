#include <iostream>
#include <cstring>
using namespace std;

const int MAX_N = 1005;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, smax, ans;
	char clabstr[MAX_N];
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		scanf("%d%s", &smax, &clabstr);
		ans = 0;
		int temp = 0;
		for (int j = 0; j < smax+1; ++j)
		{
			
			if (j > temp)
			{
				ans = ans + (j - temp);
				temp = j;
				/* code */
			}
			temp = temp + clabstr[j] - '0';
			/* code */
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
}