///     Raihan Ruhin
///     CSE, Jahangirnagar University.
///     Dhaka-Bangladesh.
///     id: raihanruhin (topcoder / codeforces / codechef / hackerrank / uva / uvalive / spoj), 3235 (lightoj)
///     mail: raihanruhin@ (yahoo / gmail / facebook)
///     blog: ruhinraihan.blogspot.com

#include<bits/stdc++.h>
using namespace std;

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define PI acos(-1.0)

#define MOD 1000000007
#define MX 100010

#define READ freopen("B-large (1).in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    READ;
    WRITE;
    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n, d, p[1005];

    cin>>tc;
    while(tc--)
    {
        cin>>d;
        int mn=0;
        for(int i=0;i<d;i++)
        {
            cin>>p[i];
            mn=max(mn, p[i]);
        }

        for(int i=2;i<=mn;i++)
        {
            int cut=0;
            for(int j=0;j<d;j++)
                if(p[j]>i)
                {
                    cut+=p[j]/i;
                    if(p[j]%i==0) cut--;
                }
            //cout<<cut<<" "<<i<<endl;
            mn=min(mn, cut+i);
        }
        //remove 1 from all
        for(int i=0;i<d;i++) if(p[i]) p[i]--;
        for(int i=2;i<=mn;i++)
        {
            int cut=0;
            for(int j=0;j<d;j++)
                if(p[j]>i)
                {
                    cut+=p[j]/i;
                    if(p[j]%i==0) cut--;
                }
            //cout<<cut<<" "<<i<<endl;
            mn=min(mn, cut+i+1);
        }
        //remove 2 from all
        for(int i=0;i<d;i++) if(p[i]) p[i]--;
        for(int i=2;i<=mn;i++)
        {
            int cut=0;
            for(int j=0;j<d;j++)
                if(p[j]>i)
                {
                    cut+=p[j]/i;
                    if(p[j]%i==0) cut--;
                }
            //cout<<cut<<" "<<i<<endl;
            mn=min(mn, cut+i+2);
        }
        cout<<"Case #"<<kk++<<": "<<mn<<"\n";
    }
    return 0;
}

