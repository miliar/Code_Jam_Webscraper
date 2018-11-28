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

char rev(char a)
{
    if(a=='+') return '-';
    return '+';
}

void solve()
{
    char a[1000];
    ss(a);
    int l = strlen(a);
    char ch = '-';
    int rs = 0;
    for(int j=l-1;j>=0;--j)
    {
        if(a[j]==ch)
        {
            ch = rev(ch);
            ++rs;
        }
    }
    printf("%d\n",rs);
}

int main()
{
    int t = 1;
    freopen("B-large.in","r",stdin);
    freopen("B-large_out.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        solve();
    }
}

