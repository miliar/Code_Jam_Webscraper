#include<bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define mmm(k,n) memset(k,n,sizeof k)
#define fast_io ios_base::sync_with_stdio(false); cin.tie(0)
#define digits(a) fixed << setprecision(a)
#define x first
#define y second

#define oo 1e9
#define pi acos(-1)
#define MOD 1000000007

using namespace std ;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
typedef pair<int, int> ii ;
typedef vector<ii> vii ;
typedef vector<int> vi ;

long long combine(long long n , int k)
{
    long long ans =1 ;
    for(int i=0 ; i< k ; i++)
        ans=(ans *(n-i))/(i+1) ;
    return ans ;
}

long long pw(long long a, long long p)
{
    if(p==0)
        return 1  ;
    if(p==1)
        return a ;
    long long half=pw(a,p/2) ;
    if(p%2==0)
        return half*half ;
    return half*half*a ;
}

long long dis(pair<long long, long long> a , pair<long long, long long> b)
{
    return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) ;
}

long long gcd(long long a, long long b)
{
    return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b)
{
    return (a*b)/gcd(a,b) ;
}

bitset<1000010> bs ;

vi sieve()
{
    vi primes ;
    long long sieve_size = 100000;
    bs.set();
    bs[0] = bs[1] = 0;
    for (long long i = 2; i <= sieve_size; i++) if (bs[i])
    {
        for (long long j = i * i; j <=sieve_size; j += i) bs[j] = 0;
        primes.push_back((int)i);
    }
    return primes ;
}

bool cmp(pair<int,int> a , pair<int,int> b)
{
    if(a.x<b.x)
        return true ;
    if(a.x==b.x)
    {
        if(a.y>b.y)
            return true ;
    }
    return false ;
}


int main() {
    //freopen("a.in","r",stdin) ;
    //freopen("a.out","w", stdout) ;
    fast_io ;
    int t ;
    cin >> t ;
    for(int o=1 ; o<=t ; o++)
    {
        string ans, s ;
        cin >> s ;
        ans+=s[0] ;
        for(int i=1 ;i<s.size() ; i++)
        {
            if(s[i]>=ans[0])
            {
                string k ;
                k+= s[i] ;
                k+=ans ;
                ans=k ;
            }
            else
            {
                ans+=s[i] ;
            }
        }

        cout << "Case #" << o <<": " << ans << endl ;
    }
    ///cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl ;
    return 0 ;
}
