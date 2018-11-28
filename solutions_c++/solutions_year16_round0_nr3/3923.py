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

ll power(ll a,ll b)
{
    ll res=1;
    //ll rm=d;
    //cout<<"pow_10 "<<rm<<endl;
    while(b>0)
    {
        if(b&1)
        {
            res=((res)*(a));
        }
        a=((a)*(a));
        b/=2;
    }
    return res;
}

ll gcd(ll a,ll b)
{
    if(a==0)
        return b;
}

void convert_binary(ll n,int bin[])
{
    vector<int> v;
    while(n>0)
    {
        int r=n%2;
        v.push_back(r);
        n/=2;
    }
    reverse(v.begin(),v.end());
    for(int i=0;i<v.size();++i)
        bin[i]=v[i];
}

ll base_z(int bin[],ll b)
{
    ll n=0;
    for(int i=0,j=15;i<16;++i,--j)
    {
        if(bin[i]==1)
            n+=power(b,j);
    }
    return n;
}

bool prime(ll n,ll fact[12],int b)
{
    if(n==2||n==3)
    return 1;
    if(n%2==0)
    {
        fact[b]=2;
        return 0;
    }
    if(n%3==0)
    {
        fact[b]=3;
        return 0;
    }
    ll i=5;
    while(i*i<=n)
    {
        if(n%i==0)
        {
            fact[b]=i;
            return 0;
        }
        if(n%(i+2)==0)
        {
            fact[b]=i+2;
            return 0;
        }
        i+=6;
    }
    return 1;
}

void print_bin(int bin[])
{
    for(int i=0;i<16;++i)
        printf("%d",bin[i]);
    printf(" ");
}
void print_fact(ll fact[])
{
    for(int i=2;i<=10;++i)
        printf("%lld ",fact[i]);
}

bool prime_bases(ll n)
{
    int bin[20];
    convert_binary(n,bin);
    ll fact[12];
    if(!prime(n,fact,2)&&!prime(base_z(bin,3),fact,3)&&!prime(base_z(bin,4),fact,4)&&!prime(base_z(bin,5),fact,5)&&!prime(base_z(bin,6),fact,6)&&!prime(base_z(bin,7),fact,7)&&!prime(base_z(bin,8),fact,8)&&!prime(base_z(bin,9),fact,9)&&!prime(base_z(bin,10),fact,10))
    {
        print_bin(bin);
        print_fact(fact);
        printf("\n");
        return 0;

    }
    return 1;
}

void solve()
{
    int cnt=0;
    ll i=0;
    while(cnt<50 && i<=32766)
    {
       ll n=i+32769;
       if(!prime_bases(n))
        ++cnt;
       i+=2;
    }
}


int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    T=1;
    int t1=1;
    while(T--)
    {
        printf("Case #%d:\n",t1++);
        solve();

    }

    return 0;
}






