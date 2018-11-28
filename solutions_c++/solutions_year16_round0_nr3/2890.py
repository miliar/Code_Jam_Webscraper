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
lol baseconv(int b, string str)
{
    int len = str.size();
    lol ans=0;

    for(int i=0;i<len; i++)
    {
        ans = ans*b+(str[i]-'0');
    }

    return ans;
}

int v[15];

int main()
{

    //READ("input.txt");
    READ("C-small-attempt0.in");
    WRITE("output.txt");


    int J,n, test,jj,len,cnt,p;
    lol dec;
    string str;

    sf("%d", &test);

    FOR1(t, test)
    {
        sf("%d %d", &n, &J);

        pf("Case #%d:\n", t);

        //n-=2;
        p = 1<<n;
        jj = 0;

        for(int i=0,j,r; i<p;i++)
        {
            str = "";
            j = i;
            cnt = 0;
            while(cnt<n)
            {
                r = j%2;
                str+=(char)(r+'0');
                j=j/2;
                cnt++;
            }
            reverse(all(str));
            len = str.size();

            if(str[0] == '0' || str[len-1]=='0')
                continue;

            cnt = 0;
            for(int b=2; b<=10; b++)
            {
                dec = baseconv(b,str);
                for(lol k=2;k<=min(100LL,dec-1);k++)
                {
                    if(dec%k == 0)
                    {
                        v[b] = k;
                        cnt++;
                        break;
                    }
                }
            }

            if(cnt == 9)
            {
                cout<<str;
                jj++;
                for(int b=2; b<=10; b++)
                    pf(" %d", v[b]);
                pf("\n");
            }

            if(jj==J)
                break;
        }
    }

    return 0;
}

