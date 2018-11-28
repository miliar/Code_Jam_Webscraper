#include<bits/stdc++.h>

#define mp make_pair
#define vi vector<int>
#define xx first
#define yy second
#define all(a) a.begin(), a.end()
#define vsort(v) sort(all(v))
#define UNIQUE(a)  sort(all(a)); a.erase(unique(all(a)), a.end())
#define clr(a,k) memset(a,k,sizeof a)
#define bclr(b) memset(b,false,sizeof b)
#define fr(i, a) for(i = 0; i < a; i++)
#define frr(i,a) for(i = a - 1; i >= 0, i--)
#define LL long long
#define ll long long
#define pb push_back
#define pii pair<int, int>
#define vll vector<long long>
///***** bit *****///
#define check_bit(a, b) (a&(1ll<<b))
#define set_bit(a, b) (a|(1ll<<b))
#define total_bit(a) __builtin_popcount(a)

#define WRITE freopen("output.txt","w",stdout)
#define use_cin  ios_base::sync_with_stdio(0); cin.tie(0);
#define READ  freopen("C-small-attempt2.in","r",stdin)

///***** Input / Output *****///
#define s1(a) scanf("%d", &a)
#define s2(a, b) scanf("%d %d", &a, &b)
#define s3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define p1(a) printf("%d", a)
#define p2(a, b) printf("%d %d", a, b)
#define p3(a, b, c) printf("%d %d %d", a, b, c)
#define eps 1e-9
#define deb cout<<"I am here"<<endl
#define MOD 1000000007
//#define MAX (lim+7)
#define INF 100000000
#define PI acos(-1.0)

using namespace std;

///******* Template ********///

template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0)return 1;
    if(e%2==0)
    {
        T t=bigmod(p,e/2,M);
        return (t*t)%M;
    }
    return (bigmod(p,e-1,M)*p)%M;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}

/**
return (a * b) % m;
where a, b, m <= 10^18
**/
template <class T> inline T multimod(T a, T b, T m)
{
    T ans = 0ll;
    a%=m, b%=m;
    while(b)
    {
        if(b&1ll) ans = m - ans > a?(ans + a): (ans + a - m);
        b >>= 1ll;
        a = (m - a)>a?a+a:a+a-m;
    }
    return (T)ans;
}


///****** fast scan ends here ***********///

//int dr[] = {-1, 0, 1, 0};
//int dc[] = {0, 1, 0, -1}; /// 4 sides
//int dr[] = {-1, -1, 0, 1, 1, 1, 0, -1}; dc[] = {0, 1, 1, 1, 0, -1, -1, -1}; /// 8 sides

#define LEN(a) strlen(a)

#define MX 100000007
#define lim 200000      /// 10^5

///***** Template ends here *****///
///********************* Code starts here ****************************

int prime[MX];
bool is[MX];
int sz;
void sieve()
{
    int sq = sqrt(MX);
    for(int j, i = 3; i <= sq; i++)
    {
        if(!is[i])
        {
            for(j = i + i; j < MX; j+= i)
                is[j] = 1;
        }
    }
    prime[sz++] = 2;
    for(int i = 3; i < MX; i+= 2)
        if(!is[i])
            prime[sz++] = i;
    return;
}


ll power(ll a, ll b)
{
    ll ret = 1ll;
    for(ll i = 0; i < b; i++)
        ret = ret * a;
    return ret;
}


bool check(ll num)
{
    ll sq = sqrt(num);
    for(int i = 0; i < sz && prime[i] <= sq; i++)
    {
        if(num%prime[i] == 0) return false;
    }
    return true;
}

ll GetDivisor(ll num)
{
    for(int i = 0; i < sz; i++)
    {
        if(num%prime[i] == 0) return prime[i];
    }
}

ll arr[100];

int main()
{
    READ;
    WRITE;
    ll  j;
    int N,  t;
    int m, cases = 1, k;
    vector<ll>ans;
    sieve();
    s1(t);
    int n, J;
    while(t--)
    {
        scanf("%d %d", &n, &J);
        ll fst = 1ll<<(ll)(n-1);
        ll lst = (1ll<<(ll)(n)) - 1ll;

        fst = fst|(1ll<<0ll);

        ans.clear();


        for(ll i = fst; i <= lst; i+=2)
        {
//            cout<<"When: "<<i<<endl;
            int ind = 0;
            ll base = 0ll;
            for(base = 2; base <= 10; base++)
            {
                ll num = 0ll;
                for(j = 0; j < n; j++)
                {
                    if(check_bit(i, j))
                        num = num + power(base, j);
                }
                if(check(num)) break;
                ll get = GetDivisor(num);
                arr[ind++] = get;
            }
            if(base == 11)
            {
                ans.pb(i);
                for(j = 0; j < ind; j++)
                    ans.pb(arr[j]);
                if(ans.size() == (J*10)) break;
            }
        }
        printf("Case #%d:\n", cases++);
        int s = ans.size();
        for(int i = 0; i < s; i+=10)
        {
            for(j = n-1; j >= 0; j--)
            {
                if(check_bit(ans[i], j))
                    cout<<1;
                else
                    cout<<0;
            }
            for(j = 1; j < 10; j++)
                cout<<" "<<ans[i+j];
            cout<<endl;
        }
    }


    return 0;
}
/*

+++-


*/
