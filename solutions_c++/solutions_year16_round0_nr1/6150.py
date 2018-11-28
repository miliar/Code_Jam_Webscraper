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

int t, cases = 0,c[15],sum;
LL n,p,q,i,j,x;
bool a[100000000];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    faster_io();
    cin >> t;
    while(t--)
    {
        cin >> n;
        memset(a, false, sizeof(a));
        memset(c, 0, sizeof(c));
        sum = 0;
        i=1;
        while(true)
        {
            q = n*i;
            p = q;
            if(a[p])
            {
                printf("Case #%d: INSOMNIA\n", ++cases);
                break;
            }
            a[p] = true;
            while(p!=0)
            {
                x = p%10;
                c[x] = 1;
                p = p/10;
            }
            for(j=0; j<=9; j++)
            {
                sum+=c[j];
            }
            if(sum == 10)
            {
                printf("Case #%d: %d\n", ++cases, q);
                break;
            }
            else
                sum = 0;
            i++;
        }
    }
    return 0;
}
