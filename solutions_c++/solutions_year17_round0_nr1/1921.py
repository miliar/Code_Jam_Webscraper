#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

#define X first
#define Y second
#define N 1010
#define M 500010

typedef long long ll;
const int INF=1ll<<30;

char s[N];

void Solve(int n,int k)
{
	if (k>n)
	{
		bool flag=true;
		for (int i=1;i<=n;i++) if (s[i]=='-') flag=false;
		if (flag) printf("0\n");
		else printf("IMPOSSIBLE\n");
		return;
	}
	int res=0; bool flag=true;
	for (int i=1;i<=n-k+1;i++)
	{
		if (s[i]=='-')
		{
			res++;
			for (int j=i;j<=i+k-1;j++)
			{
				if (s[j]=='+') s[j]='-';
				else s[j]='+';
			}
		}
	}
	for (int i=n-k+2;i<=n;i++) if (s[i]=='-') flag=false;
	if (flag) printf("%d\n",res);
	else printf("IMPOSSIBLE\n");
}

int main()
{
	//freopen("in.in","r",stdin);
	//freopen("A.out","w",stdout);
	
	int T,n,k; scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		scanf("%s%d",s+1,&k);
		n=strlen(s+1);
		Solve(n,k);
	}
	
	return 0;
}
