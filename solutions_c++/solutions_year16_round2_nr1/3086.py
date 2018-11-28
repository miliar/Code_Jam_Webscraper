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

vector<int> sieve()
{
    vi primes ;
    bitset<1000010> bs ;
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

int main() {
    //freopen("p.in","r",stdin) ;
    //freopen("a.out","w", stdout) ;
    fast_io ;
    int t ;
    cin >> t ;
    for(int o=1 ; o<=t ; o++)
    {
        string in ;
        cin >> in ;
        int x=0 ,r=0 ,u=0 , z=0, g=0 , w=0, i=0, s=0, v=0, h=0, ooo=0 ;
        string ans ;
        for(int j=0 ; j<in.size(); j++)
        {
            if(in[j]=='V')
                v++ ;
            if(in[j]=='H')
                h++ ;
            if(in[j]=='R')
                r++ ;
            if(in[j]=='U')
                u++ ;
            if(in[j]=='Z')
                z++ ;
            if(in[j]=='G')
                g++ ;
            if(in[j]=='X')
                x++ ;
            if(in[j]=='W')
                w++ ;
            if(in[j]=='S')
                s++ ;
            if(in[j]=='I')
                i++ ;
            if(in[j]=='O')
                ooo++ ;
        }

        int ff[11] ;
            mmm(ff,0) ;
            ff[0] = z ;
            ff[2] = w ;
            ff[3] = h - g  ;
            ff[4] = u ;
            ff[6] = x ;
            ff[7] = s - x ;
            ff[5] = v -ff[7] ;
            ff[8] = g ;
            ff[1] = ooo - ff[4] - ff[2] -ff[0] ;
            ff[9] = i - ff[8] -ff[6] -ff[5] ;


            for(int kk=0 ; kk<=9 ; kk++)
            {
                for(int y=0 ; y<ff[kk] ; y++)
                    ans+= kk+'0' ;
            }

        cout << "Case #" << o <<": " << ans << endl ;
    }
    ///cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl ;
    return 0 ;
}
