#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

const string mask = "1ijk";
int sign[4][4];
char mult[4][4];


int idx(char ch) {
  return mask.find(ch);
}

string tab[4][4] = {
  {"1", "i", "j", "k"},
  {"i", "-1", "k", "-j"},
  {"j", "-k", "-1", "i"},
  {"k", "j", "-i", "-1"}
};

void preprocess() {
  rep(i,4) rep(j,4) {
    if(tab[i][j][0] == '-') {
      sign[i][j] = -1;
      mult[i][j] = tab[i][j][1];
    } else {
      sign[i][j] = +1;
      mult[i][j] = tab[i][j][0];
    }
  }
}

long long L, X;
string line;

void read() {
  cin >> L >> X >> line;
}

string smult(string a, string b) {
  char pa = a.size() == 1 ? a[0] : a[1];
  int sa = a.size() == 1 ? +1 : -1;
  char pb = b.size() == 1 ? b[0] : b[1];
  int sb = b.size() == 1 ? +1 : -1;

  char ps = mult[ idx(pa) ][ idx(pb) ];
  int ss = sa * sb * sign[ idx(pa) ][ idx(pb) ];

  if(ss == -1) return string("-") + ps;
  else return string("") + ps;
}

string fpow(string num, long long x) {
  if(x == 0) return "1";
  if(x == 1) return num;
  if(x & 1) return smult(num, fpow( smult(num,num), x >> 1));
  else return fpow( smult(num,num), x >> 1);
}

map< string, map<int,int> > state[2][2];

void clear() {
  rep(i,2) rep(j,2) state[i][j].clear();
}

bool checkState(string at, int fi, int fij, int i) {
  return !state[fi][fij][at][i]++;
}

void process(int testcase) {
  int fi = 0, fij = 0, fijk = 0;
  string at = "1", fl = "";

  clear();

  for(long long x=1;x<=X;x++) for(long long i=0;i<L;i++) {

    if(!checkState(at,fi,fij,i)) {
      goto end;
    }

   // if(!state.insert(st).second) break;

    at = smult(at, string("") + line[i]);

    //dbg(x _ i _ at);

    if(fi == 0) {
      if(at.size() == 1 && at[0] == 'i') {
        fi = 1;
      }
    }
    else if(fij == 0) {
      if(at.size() == 1 && at[0] == 'k') {
        fij = 1;
      }
    }

    if(i == L-1 && x == 1) {
      fl = at;
    }
  } end:;

  fl = fpow(fl, X);

  //dbg(fl);

  if(fl.size() > 1 && fl[1] == '1') {
    fijk = 1;
  }

  

  //dbg(fi _ fij _ fijk);

  printf("Case #%d: %s\n",testcase, (fi && fij && fijk) ? "YES" : "NO");
}

int main() {
  preprocess();
  int T;
  cin >> T;
  for(int testcase=1;testcase<=T;testcase++) {
    read();
    process(testcase);
  }
  return 0;
}

