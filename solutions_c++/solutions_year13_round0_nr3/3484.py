#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;
typedef long long ll;
bool isPalindromes(ll a)
{
    if (a/10==0)
        return true;
    char g[101], c[101];
    memset(g,0x00,sizeof(g));
    memset(g,0x00,sizeof(c));
    sprintf(g,"%d",a);
    sprintf(c,"%d",a);
    string gg=g;
    string cc=c;
    reverse(cc.begin(),cc.end());
    if (gg==cc)
        return true;
    else
        return false;
}

int main()
{
	freopen("A.in","rt",stdin);
	freopen("B.out","wt",stdout);
    int t;
    std::cin>>t;
    for(int zz=0;zz<t;zz++)
    {
        ll a,b;
        cin>>a>>b;
        ll cnt=0;
        for(ll i=(ll)sqrt((double)a);i*i<=b;i++)
        {
            if (i*i>=a && i*i<=b && isPalindromes(i) && isPalindromes(i*i))
                cnt++;
        }
        cout<<"Case #"<<zz+1<<": "<<cnt<<"\n";
    }
}