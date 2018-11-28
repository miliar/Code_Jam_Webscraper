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

int n, a[1100], b[1100];

int main(){
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  int TT;
  cin>>TT;

  Rep(tt,1,TT){
    cout<<"Case #"<<tt<<": ";

    cin>>n;
    Rep(i,1,n)
      cin>>a[i];
    memset(b,0,sizeof b);
    int ans=0;
    Rep(_,1,n){
      int x=-1;
      Rep(i,1,n)
        if (!b[i] && (x==-1 || a[x]>a[i]))
          x=i;
      b[x]=1;
      int ret_l=0, ret_r=0;
      Rep(j,1,n)
        if (!b[j]){
          if (j<x)
            ret_l++;
          else
            ret_r++;
        }
      ans+=min(ret_l,ret_r);
    }
    cout<<ans<<endl;
  }

  return 0;
}
