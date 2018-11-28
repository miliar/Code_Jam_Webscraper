#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[10005];
int n,x,test;

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&test);
	for (int T = 1; T <= test; T++)
	{
		scanf("%d%d",&n,&x);
		for (int i = 0; i < n; i++) scanf("%d",s + i);
		sort(s,s + n);
		int i = 0,j = n - 1,ans = 0;
		while (i <= j)
		{
			if (i == j)
			{
				ans++;
				i++; j--;
			} else
			if (s[i] + s[j] <= x)
			{
				ans++;
				i++; j--;
			} else j--,ans++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
}
