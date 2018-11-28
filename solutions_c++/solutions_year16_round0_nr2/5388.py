#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
char str[110];
int opt[110][2];

int solve()
{
	scanf("%s",str);
	int n = strlen(str);
	memset(opt,63,sizeof(opt));
	opt[0][0] = (str[0] == '-')? 0 : 1;
	opt[0][1] = (str[0] == '+')? 0 : 1;
	
	for (int i=0;i<n;++i)
	{
		if (str[i]=='+')
		{
			opt[i][1] = min(opt[i-1][1],opt[i-1][0]+1);
			opt[i][0] = min(opt[i-1][1]+1,opt[i-1][0]+2);
		}
		else // str[i]=='-'
		{
			opt[i][0] = min(opt[i-1][0],opt[i-1][1]+1);
			opt[i][1] = min(opt[i-1][0]+1,opt[i-1][1]+2);
		}
	}
	return min(opt[n-1][1],opt[n-1][0]+1);
	
}

int main()
{
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
		printf("Case #%d: %d\n",i,solve());

	return 0;
	
}