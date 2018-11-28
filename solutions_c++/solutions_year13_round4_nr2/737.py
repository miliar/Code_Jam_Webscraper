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
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

LL calc(LL n, LL p)
{
    LL ret=0;
    vector<int> a;
    p=(1ll<<n)-p;
    LL pp=p;
    while (p>0)
    {
        a.push_back(p%2);
        p/=2;
    }
    while (a.size()<n) a.push_back(0);
    reverse(a.begin(),a.end());
    LL s=0;
    int cnt=0;
    for (int i=0;i<a.size();i++)
        {
            ret+=(1ll<<s);
            s++;
            if (a[i]==1) break;
        }
    if (pp>0) ret--;
    return ret;
}
int main()
{
    freopen("manyprizes.in","r",stdin);
    freopen("manyprizes.out","w",stdout);
    int nt, tt=1;
    cin>>nt;
    while (nt--)
    {
        LL n, p;
        cin>>n>>p;
        LL r1=calc(n,p), r2=calc(n,(1ll<<n)-p)+1;
        r2=(1ll<<n)-1-r2;
        r2=max(r2,r1);
        cout<<"Case #"<<tt++<<": "<<r1<<" "<<r2<<endl;
    }
}
