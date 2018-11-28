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

#define BIG 100
#define GOOD 0
#define NIL mp(-1, -1)
#define I first
#define J second

int lawn[BIG][BIG];
int n, m;

ii get_small(void){
  int min = 101;
  ii ret = NIL;
  rep(i, n)
    rep(j, m)
    if (lawn[i][j] != GOOD && lawn[i][j] < min){
      ret = mp(i, j);
      min = lawn[i][j];
    }
  return ret;
}

int main(void)
{
  ifstream fin;
  ofstream fout;
  fin.open("8.in");
  fout.open("8.out");
  
  int t;
  ii next;
  fin >> t;
  rep(k, t){
    fout << "Case #" << k + 1 << ": ";
    fin >> n >> m;
    rep(i, n)
      rep(j, m)
      fin >> lawn[i][j];

    while(1){
      next = get_small();
      if (next == NIL){
	fout << "YES\n";
	break;
      }
      int r, c, h;
      r = c = 0;
      h = lawn[next.I][next.J];
      rep(j, m)
	if (lawn[next.I][j] > h){
	  c++;
	  break;
	}
      rep(i, n)
	if (lawn[i][next.J] > h){
	  r++;
	  break;
	}
      if (r && c){
	fout << "NO\n";
	break;
      }
      if (!r)
	rep(i, n)
	  lawn[i][next.J] = GOOD;
      if (!c)
	rep(j, m)
	  lawn[next.I][j] = GOOD;
    }
  }

  fout.close();
  fin.close();
  return 0;
}
