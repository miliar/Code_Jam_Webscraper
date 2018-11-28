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

int T;
int n;
char S[1005];
string ans_left, ans_right;

int main() {
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%s", S);
    n = strlen(S);
    ans_left = ans_right = "";
    ans_left.push_back(S[0]);
    for (int i = 1; i < n; ++i) {
      if (S[i] >= ans_left.back()) ans_left.push_back(S[i]);
      else ans_right.push_back(S[i]);
    }
    reverse(ans_left.begin(), ans_left.end());
    printf("Case #%d: %s\n", t, (ans_left + ans_right).c_str());
  }

  return 0;
}
