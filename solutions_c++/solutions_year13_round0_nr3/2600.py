#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>

using namespace std;

#define s(n) scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)

#define pb push_back
#define mp make_pair
#define gcd __gcd
#define bitcount __builtin_popcount

#define rep(i, n) for(int i=0;i<(n);i++)
#define forall(i,a,b) for(int i=(a);i<(b);i++)
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin() ;it!=(c).end();++it)
#define all(a) (a).begin(), (a).end()
#define in(a,b) ((b).find(a) != (b).end())
#define fill(a,v) memset((a), (v), sizeof (a))
#define sz(a) ((int)((a).size()))

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs;
typedef pair<int,int> ii; 

#define BIGG 100000000000000L
#define BIG 10000000

vector <ll> squares;

bool pal(ll n){
  ll f, b, r, n2, t;
  n2 = n;
  if (n2 < 10)
    return true;
  b = n2 % 10;
  n2 /= 10;
  t = 1;
  while(n2 > 10){
    n2 /= 10;
    t *= 10;
  }
  f = n2;
  r = (n / 10) % t;

  if (f == b)
    return pal(r);
  else
    return false;
}

int main(void)
{  
  ll p;
  for (ll i = 1; i <= BIG; i++){
    p = i * i;
    if (pal(i) && pal(p))
      squares.pb(p);
  }
  ifstream fin;
  ofstream fout;
  fin.open("4.in");
  fout.open("4.out");
  
  ll a, b;
  int la, gb;
  int t;
  fin >> t;
  rep(k, t){
    fout << "Case #" << k + 1 << ": ";
    fin >> a;
    fin >> b;
    la = 0;
    while(la < squares.size() && squares[la] < a)
      la++;
    gb = squares.size() - 1;
    while(gb > 0 && squares[gb] > b)
      gb--;
    fout << gb - la + 1 << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
