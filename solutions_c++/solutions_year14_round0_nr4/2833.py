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

#define READ freopen("D-large.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    READ;
    WRITE;
    int tc,kk=1, n;
    double naomi[1010], ken[1010];
    cin>>tc;

    while(tc--)
    {
        cin>>n;
        for(int i=0;i<n;i++) cin>>naomi[i];
        sort(naomi, naomi+n);
        for(int i=0;i<n;i++) cin>>ken[i];
        sort(ken, ken+n);

        int war=0, dwar=0, pos=0;
        for(int i=0;i<n;i++)
        {
            while(ken[pos]<naomi[i] && pos<n)
            {
                pos++;
            }
            if(pos==n) {war=n-i; break;}
            pos++;
        }

        pos=0;

        for(int i=0;i<n;i++)
        {
            while(naomi[pos]<ken[i] && pos<n)
            {
                pos++;
            }
            if(pos==n) break;
            dwar++;
            pos++;
        }

        cout<<"Case #"<<kk++<<": "<<dwar<<" "<<war<<endl;
    }
    return 0;
}

