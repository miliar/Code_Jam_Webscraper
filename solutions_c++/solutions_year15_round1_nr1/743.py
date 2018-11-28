#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 1005

int N;
int m[maxN];

int main(){
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int ans1, ans2;
    scanf("%d", &N);
    REP(i, N) scanf("%d", m + i);
    ans1 = ans2 = 0;
    int mind = 0;
    REP(i, N-1) {
      if (m[i] > m[i+1]) ans1 += m[i] - m[i+1];
      mind = max(mind, (m[i] - m[i+1]));
    }

    REP(i, N-1) {
      ans2 += min(m[i], mind);
    }

    printf("Case #%d: %d %d\n", t, ans1, ans2);
  }

  return 0;
}
