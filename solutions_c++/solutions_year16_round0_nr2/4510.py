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

#define READ freopen("B-large.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

int main()
{
    READ;
    WRITE;
    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n;
    string s;
    cin>>tc;
    while(tc--)
    {
        stack<char>stk;
        cin>>s;
        for(int i=0;i<s.size();i++)
            stk.push(s[i]);

        int cnt=0;
        char now='+';
        while(!stk.empty())
        {
            while(!stk.empty() && stk.top()==now)
                stk.pop();

            cnt++;
            if(now=='+') now='-';
            else now='+';
        }

        cout<<"Case #"<<kk++<<": "<< cnt-1 <<"\n";
    }
    return 0;
}

