//C.cpp
//SmartCoder
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi=acos(-1.0);
const double eps=1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
ll res[]={1ll,4ll,9ll,121ll,484ll,10201ll,12321ll,14641ll,40804ll,44944ll,
    1002001ll,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,
    121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,
    10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,
    1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,
    1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,
    1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll,
    100000020000001ll,100220141022001ll,102012040210201ll,102234363432201ll,
    121000242000121ll,121242363242121ll,123212464212321ll,123456787654321ll,
    400000080000004ll};
int main(){
  freopen("in.txt","rt",stdin);
  freopen("out.out","wt",stdout);
  vector<ll> re(res,res+48);
  ll S,E;
  int n;
  int ret=0;
  cin>>n;
  for(int tc=1;tc<=n;++tc){
    cin>>S>>E;
    ret=0;
    for(int i=0;i<sz(re);++i){
      if(re[i]>=S&&re[i]<=E) ret++;
      if(re[i]>E) break;
    }
    printf("Case #%d: %d\n",tc,ret);
  }
  return 0;
}
