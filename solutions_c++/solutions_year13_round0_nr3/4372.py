#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 2100000000
#define eps 1e-8
#define lld long long

using namespace std;
int ok(lld x)
{
    lld m = x, l,r ,n = 0;
    lld a[20];
    while(m > 0)
    {
        a[++n] = m % 10;
        m /= 10;
    }
    l = 1;
    r = n;
    while(l < r)
    {
        if (a[l] != a[r]) return 0;
        l++;
        r--;
    }
    return 1;
}
lld n, i;
lld p[50]={1ll,4ll,9ll,121ll,484ll,
10201ll,12321ll,14641ll,40804ll,
44944ll,1002001ll,1234321ll,4008004ll,
100020001ll,102030201ll,104060401ll,121242121ll,123454321ll,
125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,
12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,
1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,
1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
int main()
{
    lld T,x,y,tot=0;
//        freopen("C.in","r",stdin);
//    freopen("a.out","w",stdout);
   cin>>T;
   while(T--)
   {
       lld ans = 0;
       cin>>x>>y;
       for(i = 0; i < 40; i++)
       if (p[i] >=x && p[i] <=y) ans++;
       printf("Case #");
       tot++;
      cout<<tot<<": "<<ans<<endl;
   }
}
