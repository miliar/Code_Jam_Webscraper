#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
char a[9999];
char b[9999];
int n, m;
int bl;
int main()
{
	int t;
	int tv = 1;

//	freopen("A-small-attempt1.in", "rt",stdin);
//	freopen("A-small-attempt1.out", "wt",stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	scanf("%d", &t);
	while (t--)
	{
		scanf("%s", a);
		for (n = 0; a[n]; n++);
		int i, j, k;
		b[0] = 0;
		bl = 0;
		for (i = n - 1; i >= 0; i--)
		{
			bool none = false;
			for (j = 0; j < bl; j++)
			{
				if (b[j] < a[i])
				{
					break;
				}
			}
			if (!none)
			{
				b[j] = a[i];
				bl = j + 1;
				b[bl] = 0;
			}
		}
		printf("Case #%d: ", tv);
		printf("%s", b);
		for (i = 0; i < n; i++)
		{
			if (bl > 0 && b[bl - 1] == a[i]) { bl--; continue; }
			else printf("%c" , a[i]);
		}
		printf("\n");
		tv++;
	}
}