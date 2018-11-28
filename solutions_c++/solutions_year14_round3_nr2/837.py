#include <iostream>
#include <sstream>
#include <string>
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
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1e+9;
const double EPS = 1e-10;
const double PI = acos(-1.0);



int main()
{
  int T; cin >> T;
  REP(tcase, T) {
    int n; cin >> n;
    vector<string> words(n);
    REP(i, n) cin >> words[i];
    
    int res = 0;
    vector<int> indices(n);
    REP(i, n) indices[i] = i;
    bool used[26];

    do {
      string sentence;
      REP(i, n) sentence += words[indices[i]];
      //dump(sentence);

      REP(c, 26) used[c] = false;
      int curr = 0;
      bool ok = true;
      while(curr < sentence.size()) {
        char c = sentence[curr] - 'a';
        if(used[c]) {
          ok = false;
          break;
        }
        else {
          used[c] = true;
          while(curr < sentence.size() && sentence[curr] - 'a' == c) curr++;
        }
      }

      if(ok) res += 1;
    } while(next_permutation(ALL(indices)));

    printf("Case #%d: %d\n", tcase + 1, res);
  }
  
  return 0;
}
