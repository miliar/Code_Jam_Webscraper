#include<bits/stdc++.h>
#define INF 1e9
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define MAXN 30
#define MAXV 30000
#define MOD 1000000007
#define get(a) geta(&a)
#define getw getchar
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define MAX 100
typedef long long lld;
using namespace std;
template<class T>
inline void geta(T* a)
{
    T n=0;
    char p;
    T s=1;
    p=getw();
    if(p=='-')
        s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
        p=getw();
    if(p=='-')
        s=-1;
    while(p>='0'&&p<='9')
    {
        n=(n<<3)+(n<<1)+p-'0';
        p=getw();
    }
    *a=n*s;
}

lld no_digits(lld a,lld b)
{
    lld ans=(int)(b*log10(a))+1;
    return ans;
}

lld pow_10(lld d)
{
    lld res=1;
    for(lld i=1;i<=d;++i)
        res*=10;
    return res;
}

lld power(lld a,lld b,lld d)
{
    lld res=1;
    lld rm=pow_10(d);
    //cout<<"pow_10 "<<rm<<endl;
    while(b>0)
    {
        if(b&1)
        {
            res=((res%rm)*(a%rm))%rm;
        }
        a=((a%rm)*(a%rm))%rm;
        b/=2;
    }
    return res;
}

lld gcd(lld a,lld b)
{
    if(a==0)
        return b;
    return gcd(b%a,a);
}

lld gcd2(lld a,lld b)
{
    while(a)
    {
        lld r=b%a;
        b=a;
        a=r;
    }
    return b;
}

string s;
int n;
int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    get(t);
    int tt=1;
    while(t--)
    {
        get(n);
        cin>>s;
        int cur_p=0;
        int fr=0;
        int i;
        for(i=0;i<=n;++i)
        {
            if(s[i]=='0')
                continue;
            int no=s[i]-'0';
            if(i<=cur_p)
                cur_p+=no;
            else
            {
                fr+=(i-cur_p);
                cur_p+=(i-cur_p+no);
            }
        }
        printf("Case #%d: %d\n",tt,fr);
        ++tt;

    }
    return 0;
}

