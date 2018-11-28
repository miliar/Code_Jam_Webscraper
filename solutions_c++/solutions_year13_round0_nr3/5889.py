#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <stack>
#include <sstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					scanf("%d",&n)
#define p(n)					printf("%d\n",n)
#define pl(n)					printf("%lld\n",n)
#define sd(n)					int n;scanf("%d",&n)
#define sl(n)					scanf("%lld",&n)
#define sld(n)					long long int n;scanf("%lld",&n)
#define pb(n)                                   push_back(n)
#define all(c)                                  (c).begin(),(c).end()
#define tr(container,it)                        for (typeof(container.begin()) it=container.begin();it!=container.end();it++ )
#define sz(a)                                   int((a).size())
#define clr(a)                                  memset(a,0,sizeof(a))
#define mp(a,b)                                 make_pair(a,b)

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vstr;

string int2str(int n)
{
    stringstream ss;
    string ans;
    ss<<n;
    ss>>ans;
    return ans;
}

bool isp(int a)
{
    string s=int2str(a);
    string s_rev=s;
    reverse(all(s_rev));
    if (s.compare(s_rev)) return false;
    return true;
}

bool isps(int a)
{
    if (isp(a)==false) return false;
    int sq=sqrt(a);
    if (sq*sq!=a) return false;
    if (isp(sq)==false) return false;
    return true;
}

int main()
{
    sd(t);
    int i;
    FOR(i,0,t)
    {
        sd(a);sd(b);
        int j;
        int ans=0;
        FOR(j,a,b+1) ans+=(isps(j));
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}
