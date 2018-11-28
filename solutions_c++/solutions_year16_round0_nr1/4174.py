#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back
#define pii pair <int, int>
#define sz(v) (int)v.size()

using namespace std;

const int MXN = (int)1e6 + 10;
const int INF = (int)1e9 + 7;
const llong LINF = (llong)1e18 + 10;
const double EPS = (double)1e-9;
const double PI = (double)acos(-1.0);

int T, n;
int cnt;
bool used[20];

void calc(llong x){
  while(x){
    if(!used[x % 10])
      ++cnt;
    used[x % 10] = true;
    x /= 10;
  }
}

int main(){
  //#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  //#endif // LOCAL
  scanf("%d", &T);
  for(int tests = 1; tests <= T; ++tests){
    scanf("%d", &n);
    printf("Case #%d: ", tests);
    if(!n){
      printf("INSOMNIA\n");
      continue;
    }
    cnt = 0;
    fill(used, used + 10, false);
    //
    for(int i = 1; i <= 1000; ++i){
      calc(i * 1LL * n);
      if(cnt == 10){
        printf("%lld\n", i * 1LL * n);
        break;
      }
    }
  }
  return 0;
}
