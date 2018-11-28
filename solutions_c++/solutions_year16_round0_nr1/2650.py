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


void solve()
{
    LL n;
    slld(n);
    if(n==0)
    {
        printf("INSOMNIA\n");
        return;
    }
    int ar[10] = {0};
    int cnt = 0;
    LL mask,i = 1;
    while(cnt<10)
    {
        mask = n*i;
        while(mask > 0)
        {
            if(ar[mask%10] == 0)
            {
                cnt++;
                ar[mask%10] = 1;
            }
            mask/=10;
        }
        i++;
    }
    printf("%lld\n",n*(i-1));

}

int main()
{
    freopen("1l.in","r",stdin);
    freopen("1l.out","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
        printf("Case #%d: ",i);
		solve();
	}
}

