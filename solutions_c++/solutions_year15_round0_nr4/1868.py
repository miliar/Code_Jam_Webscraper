#include<string>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<iostream>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<ctime>
#define LL __int64
#define eps 1e-8
#define zero(x) ((x > +eps) - (x < -eps))
#define mem(a,b) memset(a,b,sizeof(a))
#define MOD 1000000007
#define INF 99999999
#define MAX 100010
using namespace std;

char str[100010];
char s[3] = "ik";

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int t, x, r, c;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",ii);
		if(x == 1)
		{
			printf("GABRIEL\n");
		}
		else if(x == 2)
		{
			if(r * c % 2)
			{
				printf("RICHARD\n");
			}
			else
			{
				printf("GABRIEL\n");
			}
		}
		else if(x == 3)
		{
			if(r * c % 3 || r * c == 3)
			{
				printf("RICHARD\n");
			}
			else
			{
				printf("GABRIEL\n");
			}
		}
		else
		{
			if(r * c == 12 || r * c == 16)
			{
				printf("GABRIEL\n");
			}
			else
			{
				printf("RICHARD\n");
			}
		}
	}
	return 0;
}