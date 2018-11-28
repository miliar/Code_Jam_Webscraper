#include <iostream>
#include <string.h>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <limits.h>
#include <vector>
#include <string>
#include <ctype.h>
#include <complex>
#include <cmath>
using namespace             std;
const int                   Maxn=3000,Maxm=2500000,Mo=1000000007,oo=INT_MAX;
struct F {
    int c1,c2,b;
};
int                         n,m,cs,ck;
int                         can[Maxn],l,r;
bool check(int k)
{
    char a[10];
    if (k>1000) return 0;
    int p=0;
    while (k)  a[++p]=k%10+'0',k/=10;
    for (int i=1;i<=p;i++)
        if (a[i]!=a[p-i+1]) return 0;
    return 1;
}
int main()
{
    ios::sync_with_stdio(0);
//    freopen("/Users/MAC/Desktop/Error202/Error202/1.in","r",stdin);
//    freopen("/Users/MAC/Desktop/Error202/Error202/1.out","w",stdout);
    int tt=0;
    for (int i=1;i<=1000;i++)
        if (check(i)&&check(i*i))
            can[i*i]=1;
    cin>>cs;
    while (cs--)
    {
        ck=0;
        cout<<"Case #"<<++tt<<": ";
        cin>>l>>r;
        int ans=0;
        for (int i=l;i<=r;i++) if (can[i]) ans++;
        cout<<ans<<endl;
    }
}