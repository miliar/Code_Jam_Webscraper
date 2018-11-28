#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

string best[16][3];
int counta[16][3][3];

char conv(int p)
{
  if(p == 0) return 'P';
  if(p == 1) return 'R';
  return 'S';
}

int ind(char c){
  if(c=='P') return 0;
  if(c=='R') return 1;
  return 2;
}

int main() {
  freopen("A-large (2).in", "r", stdin);
  freopen("A-large (2).out", "w", stdout);
	int T;
  cin >> T;
  
  forn(i, 13)
  {
     
    forn(j, 3)
    {
      if(i)
      {
        int k=(j+1)%3;
        if(best[i-1][j]<best[i-1][k])
        {
          best[i][j]=best[i-1][j];
          best[i][j]+=best[i-1][k];
        }
        else
        {
          best[i][j]=best[i-1][k];
          best[i][j]+=best[i-1][j];
        }
      }
      else
      {
        best[i][j] = conv(j);
      }
    }
  }
  
  forn(i, 13)
  {
    forn(j, 3)
    {
      int s=best[i][j].size();
      forn(k, s)
      {
        counta[i][j][ind(best[i][j][k])]++;
      }
    }
  }
  
  forn(tc,T)
  {
    int N, R, P, S;
    cin >> N >> P >> R >> S;
    string ans = "Z";
    forn(i, 3)
    {
      //cout << best[N][i] << endl;
      if(counta[N][i][0] == R && counta[N][i][1] == P && counta[N][i][2] == S)
      {
        ans = min(ans, best[N][i]);
      }
    }
    if(ans == "Z") ans = "IMPOSSIBLE";
    cout << "Case #" << tc+1 << ": " << ans << "\n";
  }
}
