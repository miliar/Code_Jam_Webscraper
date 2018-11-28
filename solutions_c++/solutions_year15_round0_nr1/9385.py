#include <bits/stdc++.h>

using namespace std;

#define SYN ios_base::sync_with_stdio(0);cin.tie(0);
typedef long long int LLI;
typedef unsigned long long int ULLI;

#define debug(x)         cerr<<__LINE__<<" "<<#x<<" "<<x<<endl;
#define IMAX ((unsigned)1<<31)-1
#define eps 1e-11
#define fill(a,v) memset(a,v,sizeof (a))
#define SZ(X) ((int)X.size())
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define MSI map<string,int>
#define MLLI map<LLI,LLI>
#define MCI map<char,int>
#define PI acos(-1.0)
#define mk make_pair
#define pLLI pair<LLI,LLI>
#define xx first
#define yy second
#define st string

#define MOD 1000000007
#define MX 1000000
#define RADIANS(x)       (((1.0 * x * PI) / 180.0))
#define DEGREES(x)       (((x * 180.0) / (1.0 * PI)))


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for( int t=1; t<=T; t++ )
    {
        LLI n,ar[10000],add=0;
        string str;
        scanf("%lld",&n);
        cin>>str;
        if( n == 0 )
        {
            printf("Case #%d: 0\n",t);
            fill(ar,0);
            add=0;
            str.clear();
            continue;
        }
        fill(ar,0);
        for( int i=0; i<=n; i++ ) ar[i]=str[i]-'0',add+=ar[i];
        LLI s=ar[0];
        for( int i=1; i<=n; i++ )
        {
            if( ar[i] > 0 )
            {
                if( s>= i )
                {
                    s+=ar[i];
                }
                else if( s< i )
                {
                    s+=i-s;
                    //add+=i-s;
                    s+=ar[i];
                }
                //  debug(s);
            }
        }
        //cout<<add<<" "<<s<<endl;
        if( add>s ) s=0;
        else s=s-add;
        printf("Case #%d: %lld\n",t,s);
        fill(ar,0);
        add=0;
        s=0;
        str.clear();
    }
    return 0;
}

