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

#define N 1000100

int ar[100], sze;

void get(int n)
{
    for(int i=0;i<100;i++)ar[i] = 0;
    sze = 0;
    //cout<<n<<endl;
    while(n>0)
    {
        ar[sze++] = n%2;
        n/=2;
    }
}

LL calc(LL base)
{
    LL ans = 0;
    for(int i=0;i<sze;i++)
    {
        ans = ans*base + ar[i];
    }
    return ans;
}

void solve()
{
    int n,j;
    sd(n);sd(j);
    for(int i=3;i<=2*j + 1;i+=2)
    {
        get(i);
        for(int j=0;j<n/2;j++)
        {
            cout<<ar[j];
        }
        for(int i=sze;i<n/2;i++)
        {
            cout<<"0";
        }
        for(int j = 0;j<sze;j++)
        {
            cout<<ar[j];
        }
        cout<<" ";
        for(LL p=2;p<=10;p++)
        {
            printf("%lld ",calc(p));
        }
        cout<<endl;
    }

}

int main()
{
    freopen("1l.in","r",stdin);
    freopen("1l.out","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
        printf("Case #%d:\n",i);
		solve();
	}
}

