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

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

#define add(a,b) to[z] = b, ant[z] = adj[a], adj[a] = z++

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;

vector<char> A;

inline char wins(char a, char b) {
  if (a > b) swap(a,b);
  if (a == 'R' && b == 'S') return 'R';
  if (a == 'P' && b == 'S') return 'S';
  if (a == 'P' && b == 'R') return 'P';
  return 0;
}

char ch[] = {'P', 'R', 'S'};
inline int get(char c) {
  if (c == 'P') return 0;
  else if (c == 'R') return 1;
  return 2;
}

string PD[15][5];

int main() {
  rp(i,14) rp(j,3) PD[i][j] = "";
  PD[0][0] = "P";
  PD[0][1] = "R";
  PD[0][2] = "S";
  fr(i,1,14) {
    rp(a,3) fr(b,a+1,3) {
      char A = ch[a];
      char B = ch[b];
      char C = wins(A,B);
      string D1 = PD[i-1][get(A)] + PD[i-1][get(B)];
      string D2 = PD[i-1][get(B)] + PD[i-1][get(A)];
      string D = min(D1, D2);
      if (PD[i][get(C)] == "") PD[i][get(C)] = D;
      else PD[i][get(C)] = min(PD[i][get(C)], D);
    }
  }
  int t; sc(t);
  int cas = 1;
  while (t--) {
    int n; sc(n);
    int r, p, s;
    sc3(r, p, s);
    printf("Case #%d: ", cas++);
    rp(i,3) {
      int rs = 0, ss = 0, ps = 0;
      rp(j,PD[n][i].size()) {
        if (PD[n][i][j] == 'R') rs++;
        else if (PD[n][i][j] == 'S') ss++;
        else ps++;
      }
      if (rs == r && ss == s && ps == p) {
        cout << PD[n][i] << endl;
        goto fim;
      }
    }
    puts("IMPOSSIBLE");
    fim:;
  }
}






