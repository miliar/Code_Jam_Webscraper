#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define rep(i,n) for(int i=0;i<n;i++)
#define A frist
#define B second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;
    //freopen("A_1.in","r",stdin);
    //freopen("A_1_out.txt","w",stdout);

LL f[55];

LL ok1(LL m,int n)
{
    LL dayu = f[n] - m;
    LL cnt = 0;
    LL ret = 0;
    while(dayu!=1)
    {
        dayu/=2;
        cnt++;
        ret += f[n-cnt];
    }
    //cout << f[n] - ret << endl;
    return f[n] - ret;
}
LL ok(LL m,int n)
{
    LL xiaoyu = m + 1;
    LL cnt = 0;
    LL ret = 0;
    while(xiaoyu!=1)
    {
        xiaoyu/=2;
        cnt++;
        ret += f[n-cnt];
    }
    //cout << ret + 1 << endl;
    return ret + 1;
}
int main()
{
    freopen("A_2.in","r",stdin);
    freopen("A_2_out.txt","w",stdout);

    f[0]=1;
    for(int i=1;i<55;i++)f[i] = f[i-1]*2;
    int T;
    cin>>T;
    int n;
    LL p;
    rep(cas,T)
    {
        cin>>n>>p;

        LL ans1 = 0;
        LL ans2 = 0;

        LL l = 0,r = f[n],mid;
        while(l+1<r)
        {
            mid = ( l + r + 1)/2;
            if(ok(mid,n)<=p)
            {
                l = mid;
            }
            else r = mid-1;
        }

        LL l1 = 0,r1 = f[n],mid1;
        while(l1+1<r1)
        {
            mid1 = ( l1 + r1 + 1)/2;
            if(ok1(mid1,n)<=p)
            {
                l1 = mid1;
            }
            else r1 = mid1-1;
        }

        cout <<"Case #" << cas+1 << ": " << l << " " << l1 << endl;
    }
}


/*

3
3 4
3 5
3 3
*/





