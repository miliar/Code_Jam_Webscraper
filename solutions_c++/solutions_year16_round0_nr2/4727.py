#include<bits/stdc++.h>
#define INF 1e9
#define MOD 1000000007
#define get(a) geta(&a)
#define getw getchar
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
typedef long long ll;
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

ll no_digits(ll a,ll b)
{
    ll ans=(int)(b*log10(a))+1;
    return ans;
}

ll power(ll a,ll b,ll d)
{
    ll res=1;
    ll rm=d;
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

ll gcd(ll a,ll b)
{
    if(a==0)
        return b;
    return gcd(b%a,a);
}

ll solve(string& s)
{
    char prev;
    prev=s[0];
    int i=1,l=s.size();;
    while(i<l && s[i]==s[0])++i;

    ll cnt=0;
    while(i<l)
    {
        if(s[i]=='+')
        {
            cnt+=1;
            prev='+';
            int j=i+1;
            while(j<l && s[j]==s[i])++j;
            i=j;
        }
        else
        {
            cnt+=1;
            prev='-';
            int j=i+1;
            while(j<l && s[j]==s[i])++j;
            i=j;
        }
    }
    if(prev=='+')
        return cnt;
    else
        return cnt+1;
}

int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int T;
    get(T);
    int t1=1;
    while(T--)
    {
        printf("Case #%d: ",t1++);
        string s;
        cin>>s;
        printf("%lld\n",solve(s));

    }

    return 0;
}





