#include <algorithm>
#include <bitset>
#include <cctype>
#include <cerrno>
#include <clocale>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cwchar>
#include <cwctype>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <ostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,m,n) for(long long i = m; i < n; ++i)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define eps 1e-7
#define FOR(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef vector<vii> vvii;

int main() {
  ios_base::sync_with_stdio(false);
  ifstream fin("submission.in");
  ofstream fout("submission.out");
  int T;
  fin >> T;
  for (int tt = 1; tt < T + 1; ++tt) {
    ll N,M,exp=0,rea=0;
    fin>>N>>M;
    vll jin(N+1,0),chu(N+1,0);
    stack<pair<ll,ll> > st;
    rep(i,0,M){
      ll o,e,p;
      fin>>o>>e>>p;
      exp+=(2*N-e+o+1)*(e-o)*p/2;
      jin[o]+=p;
      chu[e]+=p;
    }
    rep(i,1,N+1){
      if(jin[i]>chu[i]){
        st.push(mp(i,jin[i]-chu[i]));
      }else while(jin[i]<chu[i]&&!st.empty()){
        ll a=chu[i]-jin[i];
        pair<ll,ll> tem=st.top();
        st.pop();
        ll b=min(tem.se,a);
        rea+=(2*N-i+tem.fi+1)*(i-tem.fi)*b/2;
        tem.se-=b;
        if(tem.se) st.push(tem);
        chu[i]-=b;
      }
    }
    fout << "Case #" << tt << ": "  <<exp-rea<< endl;
  }
  return 0;
}
