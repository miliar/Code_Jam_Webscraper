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

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t, n;
	char str[1010];
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%s",&n,str);
		int sum = str[0] - '0';
		int ans = 0;
		for(int i = 1; i <= n; i ++)
		{
			if(sum < i)
			{
				ans += (i - sum);
				sum = i + str[i] - '0';
			}
			else
			{
				sum += (str[i] - '0');
			}
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}