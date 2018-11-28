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

void solve()
{
	int a,b,ar[20][2],cnt=0,ans,temp;
	cin>>a;
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			cin>>temp;
			ar[temp][0]=i;
		}
	}
	cin>>b;
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			cin>>temp;
			ar[temp][1]=i;
		}
	}
	for(int i=1;i<=16;i++)
	{
		if(ar[i][0]==a&&ar[i][1]==b)
		{
			cnt++;
			ans=i;
		}
	}
	if(cnt==1)printf("%d\n",ans);
	else if(cnt==0)printf("Volunteer cheated!\n");
	else printf("Bad magician!\n");
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

