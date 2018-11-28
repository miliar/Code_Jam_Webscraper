#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
const int N = 20010;
typedef long long ll;
using namespace std;
char s[N];
bool a[N];
int main()
{
	int T,k,i1=1;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%s", s);
		scanf("%d", &k);
		int len = strlen(s);
		for (int i = 0; i < len; i++)
		{
			if (s[i] == '+')
				a[i] = 1;
			else
				a[i] = 0;
		}
		int tmp = 0;
		int flag = 1;
		for (int i = 0; i < len; i++)
		{
			if (a[i] == 0)
			{
				if (i + k > len)
				{
					flag = 0;
					break;
				}
				else
				{
					for (int j = i; j < i + k; j++)
					{
						a[j] = 1 - a[j];
					}
					tmp++;
				}
			}
		}
		printf("Case #%d: ", i1++);
		if (flag)
			printf("%d\n", tmp);
		else
			printf("IMPOSSIBLE\n");
		
	}
	return 0;
}