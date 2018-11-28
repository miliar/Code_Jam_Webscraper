#include<bits/stdc++.h>
using namespace std;

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define slld(mark) scanf("%lld",&mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define sz(x) (int((x).size()))
#define PII pair<int,int>
#define PIL pair<int,long long>
#define PLL pair<long long,long long>
#define PIS pair<int,string>
#define MII map<int,int>
#define LL long long
#define FILEIO(name) \
    freopen(name".in", "r", stdin); \
    freopen(name".out", "w", stdout);
#define INF 2000000000 // 2 * 10^9
#define INFLL 1000000000000000000LL  // 10^18
#define mod 1000000007

#define N 512345

void solve()
{
    LL n;
    bool done[10];
    memset(done,0,sizeof(done));
    slld(n);
    if(n==0)
    {
        printf("INSOMNIA\n");
        return;
    }
    int cnt = 0;
    LL ssn = n;
    n = 0;
    while(cnt<10)
    {
        n += ssn;
        //cout << " n: " << n << " cnt: " << cnt << endl;
        LL sn = n;
        while(sn)
        {
            int dig = sn%10;
            if(!done[dig])
            {
                ++cnt;
                done[dig] = 1;
            }
            sn /= 10;
        }
    }
    printf("%lld\n",n);
}

int main()
{
    int t = 1;
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        solve();
    }
}

