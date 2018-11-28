
#include <iostream>
#include <algorithm>
#include <list>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <numeric>
#include <functional>
#include <utility>
#include <iomanip>
#include <iterator>
#include <stack>
#include <limits>
#include <sstream>
#include <fstream>
#include <ostream>
#include <bitset>
#include <queue>
#include <ctime>
#include <utility>

#define inf 0x7fffffff
#define ll long long
#define re(i,j,n) for(int i=j;i<n;i++)
#define gint(n) scanf("%d",&n)
#define ms(a,n) (memset(a,n,sizeof(a)))
#define msv(a,v,n) for(int _a;_a<=n;_a++) a[_a]=v;
#define all(res) res.begin(),res.end()
#define mp(a,b) (make_pair(a,b))
#define pb(n) push_back(n)
#define loop1(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define mod 100007

using namespace std;

typedef vector< int> VI;
typedef vector< vector<int> > VVI;
typedef pair< int, int> PII;
typedef map< string, int> MSI;

ostream_iterator<int> screen(cout," ");
//copy(res.begin(),res.end(),screen);

int is_palindrom(int i, int j, string s)
{
    if(i>j) return 1;
    if(s[i]==s[j]) return is_palindrom(i+1, j-1, s);
    else return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    ll a,b,i,tmp,cnt;
    vector<ll> v;
    string s;
    stringstream ss;
    for(ll i=1; i<10000011; i++)
    {
        ss.clear();
        ss<<i;
        ss>>s;
        if(!is_palindrom(0,s.size()-1,s)) continue;
        tmp=i*i;
        ss.clear();
        ss<<tmp;
        ss>>s;
        if(!is_palindrom(0,s.size()-1,s)) continue;
        v.push_back(tmp);
    }
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        cin>>a>>b;
        cnt=0LL;
        for(int i=0; i<v.size(); i++) if(a<=v[i] && v[i]<=b) cnt++;
        printf("Case #%d: %lld\n",t,cnt);
    }
    return 0;
}
