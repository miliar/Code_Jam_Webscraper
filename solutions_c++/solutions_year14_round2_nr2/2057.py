#include<algorithm>
#include<cstdio>
using namespace std;
int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		unsigned int a, b, k;
		//change
		scanf("%d %d %d", &a, &b, &k);
		int par = 0;
		for (int j = 0; j < a; j++)
		{
			for (int l = 0; l < b; l++)
			{
				if ((j & l) < k)
					++par;
			}
		}
		printf("Case #%d: %d\n", i + 1, par);
	}
	return 0;
}