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

#define MAXN 200010

double ar[MAXN];

void solve()
{
	double c,f,x,ans=MAXN,temp;
	cin>>c>>f>>x;
	int mx=(int)(x+c+2);
	for(int i=0;i<mx;i++)
	{
		ar[i+1]=c/(i*f+2.0);
		ar[i+1]+=ar[i];
	}
	for(int i=0;i<mx;i++)
	{
		temp=x/(i*f+2.0)+ar[i];
		if(temp<ans)ans=temp;
	}
	printf("%0.7lf\n",ans);

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

