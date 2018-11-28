#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>

using namespace std;

#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 2000000009

typedef pair<int,int> PII;
typedef vector<int> VI;

#define MAXN 1010
double ar[MAXN],br[MAXN];
int cr[MAXN];

void solve()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)cin>>ar[i];
	for(int i=0;i<n;i++)cin>>br[i];
	sort(ar,ar+n);
	sort(br,br+n);
	int x=0,y=0,ans1=0,ans2=0;
	while(x<n&&y<n)
	{
		if(ar[x]<br[y])
		{
			ans1++;
			x++;y++;
		}
		else y++;
	}
	x=0;y=0;
	while(x<n&&y<n)
	{
		if(ar[x]>br[y])
		{
			ans2++;
			x++;y++;
		}
		else x++;
	}
	printf("%d %d\n",ans2,n-ans1);
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}

