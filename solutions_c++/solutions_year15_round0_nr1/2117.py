#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;

const int N = 1005;
int T , sm;
char s[N];

int main()
{
	//freopen("a.in","r",stdin); freopen("a.out","w",stdout);
	
	scanf("%d",&T);
	fo(tc,1,T)
	{
		scanf("%d",&sm);
		scanf("%s",s);
		int ans(0) , sum(0);
		fo(i,0,sm)
		if (s[i] != '0')
		{
			int t = s[i] - '0';
			if (sum < i)
				while (sum < i) sum++ , ans++;
			sum += s[i] - '0';
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	
	return 0;
}