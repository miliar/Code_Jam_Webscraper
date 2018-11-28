#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back

using namespace std;

const int INF = (int)1e9 + 7;
const int MXN = (int)1e6 + 10;
const double EPS = (double)1e-9;

int T;
int n;
char s[1001];
int ans, cur_cnt, cnt;

int main(){
  #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  scanf("%d\n", &T);
  for(int test = 1; test <= T; ++test){
    scanf("%d %s\n", &n, &s);
    cur_cnt = ans = cnt = 0;
    for(int i = 0; i <= n; ++i){
      cnt = s[i] - '0';
      if(cur_cnt >= i){
        cur_cnt += cnt;
      }
      else {
        ans += (i - cur_cnt);
        cur_cnt = i + cnt;
      }
    }
    printf("Case #%d: %d\n", test, ans);
  }
  return 0;
}
