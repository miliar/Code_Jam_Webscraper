#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define ms(x,y) memset(x,y,sizeof(x))
using namespace std;

const int N = 1005;
int a[N] , b[N];
int n , T;

void Init()
{
	scanf("%d",&n);
	fo(i,1,n) scanf("%d",&a[i]);
}

void Work(int tc)
{
	int ans , big(0);
	fo(i,1,n) big = max(big , a[i]);
	ans = big;
	fo(i,1,big)
	{
		int sum(0);
		fo(j,1,n)
		sum += (a[j]-1)/i;
		if (sum + i < ans) ans = sum + i;
	}
	printf("Case #%d: %d\n",tc,ans);
}

int main()
{
	//freopen("b.in","r",stdin); freopen("b.out","w",stdout);
	
	scanf("%d",&T);
	fo(tc,1,T)
	{
		Init();
		Work(tc);
	}
	
	return 0;
}
