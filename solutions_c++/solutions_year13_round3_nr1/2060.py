#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cstdio>
#include <unordered_map>
 
using namespace std;
 
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef long long ll;
#define PB push_back
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(), (c).end()
#define TR(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(ALL(c),x) != (c).end())
#define debug(var) cout<<#var<<"="<<(var)<<endl
 


int func()
{
  string l;
  int n;
  cin >> l >> n;
  if(n > l.size()) return 0;
  int cc(0);
  int nval(0);
  int last_chain_begin(-1);
  for(int i(0); i < l.size(); ++i) {
    if(l[i] != 'e' && l[i] != 'a' && l[i] != 'i' && l[i] != 'o' && l[i] != 'u') {
      ++cc;
      if(cc == n) {
	nval += (l.size() - i) * (1 + i - cc - last_chain_begin);
	cc--;
	last_chain_begin = i - n + 1;
      }
    } else {
      cc = 0;
    }
  }
  return nval;
}
 
int main()
{
  int t;
  cin >> t;
  for(int ti = 1; ti <= t; ti++)
    {
      cout << "Case #" << ti << ": " << func() << endl;
    }
}
