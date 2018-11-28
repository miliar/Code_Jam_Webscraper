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

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

char s[20010], t[20010];

int main()
{
	freopen("A.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%s", s);
		int n=strlen(s);
		int top=0;
		int ans=0;
		for(int i=0;i<n;i++) if (top&&s[i]==t[top-1])
		{
			top--;
			ans += 10;
		} else
			t[top++] = s[i];
		ans += top / 2 * 5;
		printf("Case #%d: %d\n", tt, ans);
	}
	
	return 0;
}