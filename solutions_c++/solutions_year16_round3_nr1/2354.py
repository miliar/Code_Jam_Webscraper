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
#define fr(i,n) for(i=1; i<=n; i++)
#define fr0(i,n) for(i=0; i<n; i++)
#define faster_io() ios_base::sync_with_stdio(false)

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    faster_io();
    int t,i,n,cases = 0,a[100],p,r,j,sum;
    cin >> t;
    while(t--)
    {
        cin >> n;
        sum = 0;
        fr0(i, n)
        {
            cin >> a[i];
            sum+=a[i];
        }
        cout << "Case #" << ++cases << ": ";
        r = 1;
        j=0;
        while(1)
        {
            fr(i, 2)
            {
                 r = *std::max_element(a,  a+n);
                 if(r==0)
                    break;
                if(r==1 && sum-j==2 && i==2)
                    break;
                 p = distance(a, max_element(a,  a+n));
                 a[p]--;
                 cout << (char)(p+65);
                 j++;
            }
            if(r==0)
                break;
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}

