///     Raihan Ruhin
///     CSE, Jahangirnagar University.
///     Dhaka-Bangladesh.
///     id: raihanruhin (topcoder / codeforces / codechef / uva ), 3235 (lightoj)
///     mail: raihanruhin@ (yahoo / gmail / facebook)
///     blog: ruhinraihan.blogspot.com

#include<bits/stdc++.h>
using namespace std;

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define PI acos(-1.0)

#define MOD 1000000007
#define MX 100010

#define READ freopen("A-large (2).in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    READ;
    WRITE;
    int digit[12];

    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n, now, tmp;

    cin>>tc;
    while(tc--)
    {
        CLR(digit);
        bool insomnia=false;
        cin>>n;
        now=n;
        int cnt=1;
        while(1)
        {
            tmp=now;
            while(tmp)
            {
                digit[tmp%10]=1;
                tmp/=10;
            }

            if((digit[0]+digit[1]+digit[2]+digit[3]+digit[4]+digit[5]+digit[6]+digit[7]+digit[8]+digit[9])==10)
            {
                break;
            }

            cnt++;
            if(cnt>1000)
            {
                insomnia=true;
                break;
            }
            now+=n;
        }

        if(insomnia)        cout<<"Case #"<<kk++<<": INSOMNIA\n";
        else         cout<<"Case #"<<kk++<<": "<< now <<"\n";
    }
    return 0;
}

