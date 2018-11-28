#include <bits/stdc++.h>
using namespace std;

const int MAXN=105;

char s[MAXN];

inline void solve()
{
	scanf("%s",s);
	int l=strlen(s),cnt=0;
	char last='0';
	for (int i=0;i<l;i++)
		if (s[i]!=last)
		{
			last=s[i];
			cnt++;
		}
	if (last=='+') cnt--;
	printf("%d\n",cnt);
}

int main()
{
//	freopen("read.txt","r",stdin);
//	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
