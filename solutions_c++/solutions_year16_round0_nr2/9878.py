#include<bits/stdc++.h>
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
#define vi vector<int>
#define vii vector< pii >

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

char S[1005];

int main() {

  int T;
  scanf("%d", &T);
  REP(t, T) {
    scanf("%s", S);
    int n = strlen(S);
    int ans = 0;
    REP(i, n) {
      if (S[i] == '-') {
        if (i == 0) ++ans;
        else if (S[i-1] == '+') ans += 2;
      }
    }
    printf("Case #%d: %d\n", t + 1, ans);
  }

  return 0;
}
