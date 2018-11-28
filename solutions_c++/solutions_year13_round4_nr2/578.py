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
string tur(ll N,ll P){
  string res(N,'0');
  ll a=N-1;
  while(P){
    if(P%2) res[a]='1';
    P/=2;
    --a;
  }
  re res;
}
int main() {
  ios_base::sync_with_stdio(false);
  ifstream fin("submission.in");
  ofstream fout("submission.out");
  int T;
  fin >> T;
  for (int tt = 1; tt < T + 1; ++tt) {
    ll N,P,res1=2,win=0;
    fin>>N>>P;
    ll res2=1ll<<N;
    string p=tur(N,P-1);
    int i;
    for(i=0;i<N&&p[i]=='1';++i) res1*=2;
    if(i==N)
      res1=res1/2-1;
    else
      res1-=2;
    bool aa=false;
    for(i=0;i<N;++i){
      if(p[i]=='1')
        aa=true;
      else{
        ++win;
        if(aa) break;
        aa=false;
      }
    }
    ll b=1;
    for(i=0;i<win;++i) b=(b<<1);
    res2-=b;
    fout << "Case #" << tt << ": "  <<res1<<' '<<res2<< endl;
  }
  return 0;
}
