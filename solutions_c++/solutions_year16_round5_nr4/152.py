#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<functional>
#include<string>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

int n,L;
map<string,int> A;
char s[100];

int main()
{
	freopen("D.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&L);
		A.clear();
		for(int i=0;i<n;i++)
		{
			scanf("%s",s);
			A[s]=1;
		}
		scanf("%s",s);
		printf("Case #%d: ", tt);
		if (A[s]==1)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (L==1)
		{
			printf("0 ?\n");
			continue;
		}
		for(int i=1;i<L;i++) printf("?");
		printf(" 10?");
		for(int i=0;i<L;i++) printf("10");
		printf("\n");
	}
	
	return 0;
}