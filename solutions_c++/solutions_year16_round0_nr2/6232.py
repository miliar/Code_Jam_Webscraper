#include<iostream>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<stdlib.h>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<utility>

using namespace std;

typedef long long LL;
typedef vector<long> Vl;
typedef vector<LL> VLL;
typedef pair<long, long> Pll;
typedef pair<LL, LL> PLL;

#define pi 4*atan(1)
#define pre setprecision(10)
#define pb push_back
#define sz(a) ((long)a.size())
#define all(c) c.begin(), c.end()
#define rall(c) c.rbegin(), c.rend()
#define sqr(a) ((a)*(a))
#define fr(m,n) for(int i=m; i<=n; i++)
#define fr0(m,n) for(int i=m; i<n; i++)
#define faster_io() ios_base::sync_with_stdio(false)

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    faster_io();
    int t,n,p,result,cases = 0,i;
    string s;
    cin >> t;
    while(t--)
    {
        cin >> s;
        p = 0;
        result = 0;
        n = s.size();
        for(i=0; i<n; i++)
        {
            if(s[i] == '+')
                p = 1;
            else if(s[i] == '-' && p==1)
            {
                result+=2;
                p = 0;
            }
        }
            if(s[0] == '-')
                result += 1;
        printf("Case #%d: %d\n", ++cases, result);
    }
    return 0;
}
