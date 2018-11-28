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

string flip(string s)
{
    for(int j=0 ; j<s.size() ; j++)
    {
        if(s[j]=='+') s[j]='-' ;
        else s[j]='+' ;
    }
    reverse(s.begin(),s.end()) ;
    return s ;
}

int main() {
    freopen("a.in","r",stdin) ;
    freopen("a.out","w", stdout) ;
    fast_io ;
    int t ;
    string s ;
    cin >>t ;

    for(int o=1 ; o<=t ;o++)
    {
        cin >> s ;
        long long ans =0 ;
        string target = "" ;
        for(int i=0 ;i<s.size() ; i++)
            target+='+' ;
        while(s!=target || s=="" )
        {
            //cout << s << endl ;
            while(s[s.size()-1]=='+')
                s.erase(s.size()-1,1) ;
            target = "" ;
            for(int i=0 ;i<s.size() ; i++)
                target+='+' ;
            if(s[0]=='+')
            {
                int j=0 ;
            while(s[j]!='-')
                j++ ;
            for(int k=0 ; k<j ; k++)
                s[k]='-' ;
            ans++;
            }
            s= flip(s) ;
            ans++;
        }

        cout << "Case #"<< o << ": " << ans << endl ;
    }
    ///cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl ;
    return 0 ;
}
