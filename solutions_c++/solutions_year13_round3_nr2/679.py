#include <cstdio>
#include <algorithm>

const int MAXN = 2e2+10;

using namespace std;

int x,y;
char sol[MAXN];

int main()
{
	int cas;
	scanf("%d",&cas);
	for(int num = 1 ; num <= cas ; num++)
	{
		scanf("%d %d",&x,&y);

		int now = 1;
		for(int c = 0 ; c < x ; c++)
		{
			sol[now++] = 'W';
			sol[now++] = 'E';
		}
		for(int c = 0 ; c < -x ; c++)
		{
			sol[now++] = 'E';
			sol[now++] = 'W';
		}
		for(int c = 0 ; c < y ; c++)
		{
			sol[now++] = 'S';
			sol[now++] = 'N';
		}
		for(int c = 0 ; c < -y ; c++)
		{
			sol[now++] = 'N';
			sol[now++] = 'S';
		}
		sol[now] = '\0';

		printf("Case #%d: %s\n", num,sol+1);
	}
}