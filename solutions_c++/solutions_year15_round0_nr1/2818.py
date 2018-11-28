#define MAXN 1001
#include <cstdio>

int ntest;
int n;
char shyness[MAXN + 5];

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%d %s", &n, shyness);
		int ninvite = 0;
		int total = 0;
		for(int i = 0;i <= n;++i)
		{
			int shy = shyness[i] - '0';
			if(shy > 0 &&  total + ninvite < i)
				ninvite += i - total - ninvite;
			total += shy;
		}
		printf("Case #%d: %d\n", test, ninvite);
	}
}
