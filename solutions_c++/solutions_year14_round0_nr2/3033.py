///     Raihan Ruhin
///     CSE, Jahangirnagar University.
///     Dhaka-Bangladesh.
///     id: raihanruhin (topcoder / codeforces / codechef / hackerrank), 3235 (lightoj)
///     mail: raihanruhin@ (yahoo / gmail / facebook)
///     blog: ruhinraihan.blogspot.com

#include<bits/stdc++.h>
using namespace std;

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define PI acos(-1.0)

#define MOD 1000000007
#define MX 100010

#define READ freopen("B-large.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    READ;
    WRITE;
    int tc,kk=1, n;
    double ta[MX], da[MX], C, F, X;
    cin>>tc;
    ta[0]=0;
    da[0]=2;
    while(tc--)
    {
        cin>>C>>F>>X;
        for(int i=1;i<=100002;i++)
        {
            ta[i]=ta[i-1]+C/da[i-1];
            da[i]=da[i-1]+F;
        }

        double mn=10000000010.2;
        for(int i=0;i<=100002;i++)
            mn=min(mn, ta[i]+X/da[i]);

        cout<<"Case #"<<kk++<<": "<<setprecision(8)<<fixed<<mn<<endl;
    }
    return 0;
}

