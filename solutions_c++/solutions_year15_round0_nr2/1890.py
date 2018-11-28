#include<bits/stdc++.h>

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

#define N 1010

int ar[N];

void solve()
{
    int n,mx=0,tmp=0,ans=INF;
    sd(n);
    for(int i=0;i<n;i++)
    {
        sd(ar[i]);
        mx=max(ar[i],mx);
    }
    for(int i=1;i<=mx;i++)
    {
        tmp=i;
        for(int j=0;j<n;j++)
        {
            tmp=tmp + ((ar[j]-1)/i);
        }
        ans = min(tmp,ans);
    }
    cout<<ans<<endl;
}

int main()
{
    //freopen("in2.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
        printf("Case #%d: ",i);
		solve();
	}
}

