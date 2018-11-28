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

#define READ freopen("D-small-attempt0.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    READ;
    WRITE;
    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n, x, r, c;
    string s;
    cin>>tc;
    while(tc--)
    {
        cin>>x>>r>>c;
        if(c>r) swap(r, c);
        if(x==1) s="GABRIEL";
        else if(x==2)
        {
            if((r*c)%2==0)
                s="GABRIEL";
            else s="RICHARD";
        }
        else if(x==3)
        {
            if((r*c)%3==0)
            {
                if(!(r==3 && c==1))
                  s="GABRIEL";
                else s="RICHARD";
            }
            else s="RICHARD";
        }
        else
        {
            if((r*c)%4==0)
            {
                if(r==4 && c>=3)
                    s="GABRIEL";
                else s="RICHARD";
            }
            else s="RICHARD";
        }
        cout<<"Case #"<<kk++<<": "<<s<<"\n";
    }
    return 0;
}

