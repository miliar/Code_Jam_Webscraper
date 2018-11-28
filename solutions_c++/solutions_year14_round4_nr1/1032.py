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

#define MAXN 10010

int ar[MAXN];

int gcd(int a,int b)
{
    if(b==0)return a;
    else return gcd(b,a%b);
}

void solve()
{
    int n,x;
    sd(n);sd(x);
    for(int i=0;i<n;i++)sd(ar[i]);
    sort(ar,ar+n);
    int cnt=n,a=0,b=n-1,ans=0;
    while(cnt>1)
    {
        if(ar[a]+ar[b]<=x)
        {
            a++;b--;cnt-=2;
        }
        else
        {
            b--;cnt--;
        }
        ans++;
    }
    printf("%d\n",ans+cnt);
}

int main()
{
    //freopen("in1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
	    printf("Case #%d: ",i);
		solve();
	}
}

