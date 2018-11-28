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

#define READ freopen("A-large.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)


int main()
{
    READ;
    WRITE;
    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n, smax;
    string s;

    cin>>tc;
    while(tc--)
    {
        vector<int>v;
        cin>>smax;
        cin>>s;
        for(int i=0;i<=smax;i++)
        {
            int k=s[i]-'0';
            for(int j=0;j<k;j++)
                v.push_back(i);
        }
        sort(v.begin(), v.end());
        int req=0, aud=0;
        int vl=v.size();
        for(int i=0;i<vl;i++)
        {
            if(v[i]>aud)
            {
                req+=v[i]-aud;
                aud=v[i];
            }
            aud++;
        }

        cout<<"Case #"<<kk++<<": "<<req<<"\n";
    }
    return 0;
}

