#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <climits>
#include <assert.h>

using namespace std;


typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> int2;
typedef pair<float, float> float2;
typedef pair<ull, ull> ull2;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define del(s,x) do {__typeof((s).begin()) abcde=(s).find(x); if(abcde !=(s).end()) s.erase(abcde); } while(0);
#define del2(s,x) do {__typeof((s).begin()) abcde=find(all(s),x); if(abcde !=(s).end()) s.erase(abcde); } while(0);
 
template<class T> inline bool comp(T a, T b) {return a>b;} // sort(t, t+9, comp<int>);

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

void reorder (string &s, int deb, int fin) {
  
  if (fin - deb < 2) return;
  int midlen = (fin - deb) / 2;
  reorder (s, deb, midlen);
  reorder (s, deb + midlen, fin);
  //if (deb == 0 && fin == 4 && s == "RSPS")
  // cout << "la " << s << endl;
  FOR(i,deb,deb+midlen) {
    if (s[i] < s[i+midlen])
      return;
    else if (s[i] > s[i + midlen]) {
      FOR(k,i,deb+midlen) {
	char tmp = s[k];
	s[k] = s[k+midlen];
	s[k+midlen] = tmp;
      }
    }
  }
}
string solve (int n, char init) {
  string s(1,init);
  FOR(i,0,n) {
    string snew = "";
    FOR(j,0,s.size()) {
      if (s[j] == 'P') snew += "PR";
      else if (s[j] == 'R') snew += "RS";
      else {
	assert(s[j] == 'S');
	snew += "PS";
      }
    }
    swap (s, snew);
  }
  //cout << "ici " << s << endl;
  reorder (s, 0, s.size());
  return s;
}

int main() {
  int T;
  cin >> T;
  cout.precision(12);
  int N, R, P, S;
  FOR (test, 1, T+1) {
    cin >> N >> R >> P >> S;
    vector<string> s (3, "");
    s[0] = solve(N,'P');
    s[1] = solve(N,'R');
    s[2] = solve(N,'S');
    sort (all(s));
    bool ok = false;
    FOR(k,0,3) {
      vector<int> occ(26,0);
      FOR(i,0,s[k].size()) occ[(int)(s[k][i]-'A')] ++;
      if ((occ[(int) ('P'-'A')] == P) && (occ[(int) ('R'-'A')] == R) && (occ[(int) ('S'-'A')] == S)) {
	ok = true;
	cout << "Case #" << test << ": " << s[k] << endl;
	break;
      }
    }
    if (!ok)  cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
  }
  return 0;
}
