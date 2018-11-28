#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ld> vld;
typedef set<ld> sld;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

ll fact(int n) {
  if (n <= 1) return 1;
  return (n * fact(n-1)) % 1000000007;
}

ll solveCase() {
  int w;
  cin >> w;

  int same[26]; FOR(i, 26) same[i] = 0;
  bool edge[26][26]; FOR(i, 26) FOR(j, 26) edge[i][j] = false;
  bool middle[26]; FOR(i, 26) middle[i] = false;
  bool start[26], end[26]; FOR(i, 26) start[i] = end[i] = false;
  vector<string> words;
  FOR (i, w) {
    string word; cin >> word; words.pb(word);
  }
  FOR(i, w) {
    string word = words[i];
    cerr << word << endl;
    vi chars;
    FOR(i, s(word)) chars.pb(word[i] - 'a');
    bool tm[26]; FOR(i, 26) tm[i] = false;
    int first = chars[0];
    int last = chars[chars.size() - 1];
    bool atstart[26], atend[26], atmid[26]; FOR(i, 26) atstart[i] = atend[i] = atmid[i] = false;
    FOR(i, s(word)) {
      int what = chars[i];
      if (i == 0) {
        atstart[what] = true;
      }
      
      if (i == (s(word) - 1)) {
        atend[what] = true;
      }

      if (atmid[what] && (i != 0) && (chars[i-1] != what)) return 0;
      atmid[what] = true;
    }

    FOR(i, 26) {
      atmid[i] = atmid[i] && !(atstart[i] || atend[i]);
    }

    FOR(i, 26) {
      if (atmid[i] || atstart[i] || atend[i]) {
        if (middle[i]) return 0;

        if (atstart[i] && !atend[i] && start[i]) return 0;
        if (atend[i] && !atstart[i] && end[i]) return 0;
      }
    }

    FOR(i, 26) {
      start[i] = start[i] || (atstart[i] && !atend[i]);
      end[i] = end[i] || (atend[i] && !atstart[i]);
      middle[i] = middle[i] || atmid[i];
    }

    cerr << "first = " << first << "   ;    " << " last = " << last << endl;
    FOR(i, 26) {
      if (middle[i]) cerr << "m " << i << endl;
      if (start[i]) cerr << "s " << i << endl;
      if (end[i]) cerr << "e " << i << endl;
    }

    if (first == last) same[first]++;
    else {
      edge[first][last] = true;
    }
  }
  bool closure[26][26]; FOR(i, 26) FOR(j, 26) {
    if (edge[i][j]) {
      cerr << "edge " << i << ' ' << j << endl;
    }
    closure[i][j] = edge[i][j];
  }
  FOR(i, 26) FOR(j, 26) FOR(k, 26) {
    bool z = (closure[j][i] && closure[i][k]);
    closure[j][k] = closure[j][k] || z;
  }
  FOR(i, 26) if(closure[i][i]) {
    cerr << "self loop " << ('a' + i) << endl;
    return 0;
  }
  int nC = 0;
  bool seen[26]; FOR(i, 26) seen[i] = false;
  FOR(i, 26) {
    if (!seen[i]) {
      seen[i] = true;
      bool incoming = false;
      FOR(j, 26)
        if (edge[j][i]) {
          if (incoming) {
            cerr << "too many incoming " << ('a' + i) << endl;
            return 0;
          }
          incoming = true; 
        }
      if (!incoming) {
        int cur = i;
        int numCurrent = 0;
        while (true) {
          int next = -1;
          bool outgoing = false;
          FOR(j, 26) if (edge[cur][j]) {
            if (outgoing) {
              cerr << "too many outgoing " << ('a' + cur) << endl;
              return 0;
            }
            outgoing = true;
            next = j;
          }
          if (next == -1) break;
          cur = next;
          numCurrent++;
        }
        if (numCurrent > 0 || (same[i] > 0)) nC++;
      }
    }
  }

  cerr << "nc = " << nC << endl;

  ll ret = fact(nC);
  FOR(i, 26) {
    if (same[i] > 0) cerr << "same " << i << ' ' << same[i] << endl;
    ret = (ret * fact(same[i])) % 1000000007;
  }
  return ret;
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    cout << "Case #" << test << ": " << solveCase() << endl;
  }
  return 0;
}
