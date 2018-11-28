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
    bool h[2510];
    int i,j,n,t,cases = 0,a[110],x;
    cin >> t;
    while(t--)
    {
        cin >> n;
        memset(h, 0, sizeof(h));
        memset(a, 0, sizeof(a));
        for(i=0; i<(n*2-1); i++)
        {
            for(j=0; j<n; j++)
            {
                cin >> x;
                if(h[x])
                    h[x] = 0;
                else
                    h[x] = 1;
            }
        }
        j = 0;
        for(i=1; i<=2510; i++)
        {
            if(h[i])
                a[j++] = i;
        }
        sort(a, a+n);
        cout << "Case #" << ++cases << ": ";
        for(i=0; i<n; i++)
            cout << a[i] << " ";
        cout << endl;
    }
    return 0;
}
