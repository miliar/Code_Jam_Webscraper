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

int n,j ;

long long superPrime(long long a)
{
    for(long long i=2 ; i*i<=a ; i++)
    {
        if(a%i==0)
            return i ;
    }
    return 0 ;
}

long long valid(string s , int base)
{
    long long neo = 0 ;
    for(int i=s.size()-1 ;i>=0 ; i--)
    {
        if(s[i]=='1')
            neo+=pw(base,n-1-i) ;
    }
    //cout << "jamicon " << s << " base " << base << " neo " << neo << endl ;
    return superPrime(neo) ;
}

vector< pair< string,vector<long long> > > ans ;

void construct(string s)
{
    if(ans.size()==j)
        return ;
    if(s.size()==n)
    {
        if(s[0]=='1' && s[n-1]=='1')
        {
            vector<long long> v ;
            for(int i=2 ; i<=10 ; i++)
            {
                long long h = valid(s,i) ;
                if(h==0)
                    break ;
                else
                    v.push_back(h) ;
            }
            if(v.size()==9)
                ans.push_back(make_pair(s,v)) ;
        }
        return ;
    }
    s.append("0") ;
    construct(s) ;
    if(ans.size()==j)
        return ;
    s[s.size()-1]='1' ;
    construct(s) ;
}

int main() {
    //freopen("a.in","r",stdin) ;
    //freopen("a.out","w", stdout) ;
    fast_io ;
    int t ;
    string s ;
    cin >>t ;
    for(int o=1 ; o<=t ;o++)
    {
        cin >> n >> j ;
        construct("") ;
        cout << "Case #"<< o << ": " << endl ;
        for(int i=0 ; i<j ; i++)
        {
            cout << ans[i].x << ' ' ;
            for(int k=0 ;k<ans[i].y.size() ; k++)
            {
                cout << ans[i].y[k] << ' ' ;
            }
            cout << endl ;
        }
    }
    ///cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl ;
    return 0 ;
}
