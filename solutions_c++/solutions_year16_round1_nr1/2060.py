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
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    faster_io();
    string s,r;
    int t,i,n,p,cases = 0;
    cin >> t;
    while(t--)
    {
        cin >> s;
        n = s.size();
        r.clear();
        p = (int) s[0];
        for(i=0; i<n; i++)
        {
            if((int)s[i]>=p)
            {
                r = s[i] + r;
                p = (int) s[i];
            }
            else
            {
                r = r + s[i];
            }
        }
        cout << "Case #" << ++cases << ": " << r << endl;
    }
    return 0;
}

