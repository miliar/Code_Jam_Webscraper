#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) ((int)(a).size())
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
#define online1
#define RAND ((rand()<<15)+rand())
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;

int n, S;
multiset<int> a;

int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int TT;
  cin>>TT;

  Rep(tt,1,TT){
    cout<<"Case #"<<tt<<": ";

    cin>>n>>S;
    Rep(i,1,n){
      int x;
      cin>>x;
      a.insert(x);
    }
    
    int ans=0;
    while(a.size()){
      auto it=a.end(); it--;
      auto x=*(it);
      a.erase(it);
      ans++;
      auto it2=upper_bound(a.begin(), a.end(), S-x);
      if (it2!=a.begin()){
        it2--;
        a.erase(it2);
      }
    }
    cout<<ans<<endl;
  }

  return 0;
}
