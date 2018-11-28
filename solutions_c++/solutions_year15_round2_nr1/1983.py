
/*
 Problem name :
 Algorithm : Not Sure Yet
 Contest/Practice :
 Source :
 Comment : Whenever you start to believe  yourself, people also start to believe in you
 Date : --
 Last Update : 25-Mar-2015
*/

#include<bits/stdc++.h>

#define pause           system("pause");
#define FOR(s,e,inc)    for(int i=s;i<=e;i+=inc)
#define mod             1000000007
#define inf             1<<30
#define pb              push_back
#define ppb             pop_back
#define mp              make_pair
#define F               first
#define S               second
#define sz(x)           ((int)x.size())
#define sqr(x)          ( (x)* (x) )
#define eps             1e-9
#define lcm(x,y)        (abs(x) /gcd(x,y))* abs(y)
#define on(x,w)         x|(1<<w)
#define check(x,w)      (x&(1<<w))
#define all(x)          (x).begin(),(x).end()
#define pf              printf
#define pi              acos(-1.0)
#define reset(x,v)      memset(x,v,sizeof(x));
#define AND             &&
#define OR              ||
#define what_is(x)      cerr<<#x<<" is "<<x<<"\n";

typedef long long ll;
typedef unsigned long long llu;

using namespace std;


template<class T>
inline T mod_v(T num)
{
    if(num>=0)
        return num%mod;
    else
        return (num%mod+mod)%mod;
}
template<class T>
inline T gcd(T a,T b)
{
    a=abs(a);
    b=abs(b);

    while(b)
    {
        a=a%b;
        swap(a,b);
    }

    return a;
}

template<class T>
T fast_pow(T n , T p)
{
    if(p==0) return 1;
    if(p%2)
    {
        T g=mod_v ( mod_v(n) * mod_v(fast_pow(n,p-1)) );
        return g;
    }
    else
    {
        T g=fast_pow(n,p/2);
        g=mod_v( mod_v(g) * mod_v(g) ) ;
        return g;
    }
}

template<class T>
inline T modInverse(T n)
{
    return fast_pow(n,mod-2);
}

template<class T>
inline void debug(string S1,T S2,string S3)
{
    cout<<S1<<S2<<S3;
}

bool equalTo ( double a, double b ){ if ( fabs ( a - b ) <= eps ) return true; else return false; }
bool notEqual ( double a, double b ){if ( fabs ( a - b ) > eps ) return true; else return false; }
bool lessThan ( double a, double b ){ if ( a + eps < b ) return true; else return false; }
bool lessThanEqual ( double a, double b ){if ( a < b + eps ) return true;   else return false;}
bool greaterThan ( double a, double b ){if ( a > b + eps ) return true;else return false;}
bool greaterThanEqual ( double a, double b ){if ( a + eps > b ) return true;else return false;}


template<class T>
inline T in()
{
    register char c=0;
    register T num=0;
    bool n=false;
    while(c<33)c=getchar();
    while(c>33){
        if(c=='-')
            n=true;
        else num=num*10+c-'0';
        c=getchar();
    }
    return n?-num:num;
}

/******* ! Code start from here ! *******/

ll rev(ll v)
{
    ll x=0;
    while(v>0)
    {
        x=x*10+(v%10) ;
        v/=10;
    }

    return x;
}

int dp[1000009];
int done[1000009]={0},CC=1;
ll n;

int re(ll num)
{    if(num==n) return 0;
    else if(num>n) return inf;

    if(done[num]==CC) return dp[num];

    done[num]=CC;

    dp[num]=inf;

    if(rev(num)>num)
    {
        dp[num]=min(dp[num],1+re(rev(num) ) );
    }

    dp[num]=min(dp[num],1+re(1+num) );

    return dp[num];

}

int main()
{
//     std::ios_base::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen ( "A-small-attempt1.in", "r", stdin );
        freopen ( "A-small-attempt1out.out", "w", stdout );
    #endif

    int t=in<int>(),tcase=1;


    while(t--)
    {
        n=in<ll>();
        printf("Case #%d: %d\n",tcase++,re(1)+1 );

        CC++;
    }


    return 0;
}


