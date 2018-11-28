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

const ll INF = 1000000000000;
const double PI = 4 * atan(1.0);

int main() {
  ios_base::sync_with_stdio(false);
  ofstream fout("submission.out");
  int T;
  cin >> T;
  for (int num = 1; num < T + 1; ++num) {
    int r,c;
    cin>>r>>c;
    vvi st(r,vi(c)), ok(r,vi(c,0));
    rep(i,0,r)
      rep(j,0,c)
        cin>>st[i][j];
    rep(i,0,r){
      int com=*max_element(all(st[i]));
      rep(j,0,c)
        if(st[i][j]==com)
          ok[i][j]=1;
    }
    rep(j,0,c){
      int com=0;
      rep(i,0,r) com=max(com,st[i][j]);
      rep(i,0,r)
        if(st[i][j]==com)
          ok[i][j]=1;
    }
    int res=1;
    rep(i,0,r)
      rep(j,0,c)
        res =res&&ok[i][j];
    fout<<"Case #"<<num<<": "<<(res?"YES":"NO")<<endl;
  }
  return 0;
}
