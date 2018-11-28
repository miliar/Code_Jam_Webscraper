#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007

int a[100][100],cnt[10010],ans[100];
int n,m;



int main()
{
	int T;
	scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d",&n);
		m=2*n-1;
		clr(cnt,0);
		int t;
		rep(i,1,m)rep(j,1,n)
		{
			scanf("%d",&t);
			cnt[t]++;
		}
		int tot=0;
		rep(i,1,2500)if(cnt[i]&1)ans[++tot]=i;
		sort(ans+1,ans+1+tot);
		
		printf("Case #%d: ",ii);
		rep(i,1,tot)printf("%d%c",ans[i],i==tot?'\n':' ');
	}
	
	return 0;
}
