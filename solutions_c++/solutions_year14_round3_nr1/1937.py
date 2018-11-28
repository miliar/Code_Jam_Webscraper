//A0.cpp
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
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
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
int main(){
  std::ios_base::sync_with_stdio(0);
  freopen("A0.txt","w",stdout);
  freopen("A-small-attempt0.in","r",stdin);
  int tc;
  cin>>tc;
  ll rs=0;
  ll a,b,at,bt;
  char ch;
  for(int T=1;T<=tc;++T){
    rs=0;
    cin>>a;
    cin>>ch;
    cin>>b;
    bool flg=true;
    bool near=true;
    map<pair<ll, ll> , int> cycle;
    ll res=-inf;
    bool cy=false;
    while(true){
      rs++;
      a*=2;
      at=a;
      bt=b;
      a=a/__gcd(at,bt);
      b=b/__gcd(at,bt);
      if(cycle.count(mp(a,b))){
        cy=true;
        break;
      }
      cycle[mp(a,b)]=1;
      if(a>b){
        a-=b;
        if(near){
          near=false;
          res=rs;
        }
      }else if(a==b&&a==1){
        if(near){
          near=false;
          res=rs;
        }
        break;
      }

    }
    if(cy) cout<<"Case #"<<T<<": "<<"impossible"<<endl;
    else if(res==-inf) cout<<"Case #"<<T<<": "<<"impossible"<<endl;
    else cout<<"Case #"<<T<<": "<<res<<endl;
  }
  return 0;
}
