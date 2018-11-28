#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

void solve(int tc){
  int P[16], S[16], a1, a2;
  memset(P, 0, sizeof(P));
  memset(S, 0, sizeof(S));
  cin >> a1;
  FOR(i, 4) FOR(j, 4){
      int x;
      cin >> x;
      if (i + 1 == a1) P[x-1] = 1;
  }
  cin >> a2;
  FOR(i, 4) FOR(j, 4){
      int x;
      cin >> x;
      if (i + 1 == a2) S[x-1] = 1;
  }
  cout << "Case #" << tc << ": ";

  int cislo = -1;
  FOR(i, 16) if (S[i] == 1 && P[i] == 1){
    if (cislo == -1) cislo = i + 1;
    else{
      cout << "Bad magician!" << endl;
      return;
    }
  }

  if (cislo == -1) cout << "Volunteer cheated!" << endl;
  else cout << cislo << endl;
}

int main(){
  int TT;
  cin >> TT;
  FOR(tc, TT) solve(tc+1);
  return 0;
}
