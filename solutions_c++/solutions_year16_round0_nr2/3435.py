/* Have courage and be kind*/
#include<bits/stdc++.h>
#include<stdlib.h>
#include <assert.h>  //assert ( n >= 1 && n < 100005 );
using namespace std;
#define inf 2147383647LL
#define SET(a) memset(a,-1,sizeof(a))
#define all(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define sz(x) ((int)x.size())
#define PB push_back
#define MP make_pair
#define pii pair<int,int>
#define FOR0(i,n) for(int i = 0;i<n;i++)
#define FOR1(i,n) for(int i = 1;i<=n;i++)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define PI acos(-1.0)
#define EPS 1e-9
#define UNIQUE(V) (V).erase(unique((V).begin(),(V).end()),(V).end())//vector must be sorted
#define NUMDIGIT(x,y) (((int)(log10((x))/log10((y))))+1)
#define LCM(x,y) (((x)/gcd((x),(y)))*(y))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define lol long long
#define ulol unsigned long long
#define pf printf
#define sf scanf
#define mod 1000000007 //10^9+7
#define pause system("pause")
#define F first
#define S second
#define phl printf ( "hello\n" )
#define POPCOUNT __builtin_popcountll
#define RIGHTMOST __builtin_ctzll
#define LEFTMOST(x) (63-__builtin_clzll((x)))

lol mod_v(lol num)
{
    if(num>=0)
      return(num%mod);
    else
     return(num%mod+mod)%mod;
}

lol bigmod ( lol b, lol p, lol m ) {  //Repeated Squaring Method for Modular Exponentiation
    lol res = 1 % m, x = b % m;
    while ( p ) {
        if ( p & 1 ) res = ( res * x ) % m;
        x = ( x * x ) % m;
        p >>= 1;
    }
    return res;
}

/********** Solution ***************/
int main()
{

    //READ("B-small-attempt0.in");
    READ("B-large.in");
    WRITE("output.txt");

    int test, len, c;
    lol ans;
    string s, str, temp;

    sf("%d", &test);

    FOR1(t, test)
    {
        cin>>str;

        len = str.size();

        temp = "";
        FOR0(i, len)
         temp +='+';

        ans = 0;

        while(1)
        {
            if(str == temp)
             break;

            if(str[0] == '-')  //Flip the whole string
            {
                c = 0;
                while(str[c] == '-')
                {
                    c++;
                }
                for(int i=0;i<c;i++)
                    str[i] = '+';
            }

            else
            {
                c = 0;
                while(str[c] == '+')
                {
                    c++;
                }
                for(int i=0;i<c;i++)
                    str[i] = '-';
            }

            ans++;
        }

        pf("Case #%d: %lld\n", t, ans);
    }

    return 0;
}

