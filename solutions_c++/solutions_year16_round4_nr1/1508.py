#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair< ll, ll > ii;
typedef vector< ll > vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
//////////////////////

bool verify;
vector< string > ans;

bool ok(string at) {
  if(at.size() == 1) return true;
  string novo = "";
  for(int i = 0; i < at.size(); i+=2) {
    if((at[i] == 'R' && at[i + 1] == 'S') || (at[i] == 'S' && at[i + 1] == 'R')) novo.pb('R');
    else if((at[i] == 'P' && at[i + 1] == 'S') || (at[i] == 'S' && at[i + 1] == 'P')) novo.pb('S');
    else if((at[i] == 'R' && at[i + 1] == 'P') || (at[i] == 'P' && at[i + 1] == 'R')) novo.pb('P');
    else return false;
  }
  return ok(novo);
}

void back(int q, int p, int r, int s, string str) {
  if(q == 0) {
    if(ok(str)) {
      ans.pb(str);
      verify = 1;
    }
    return;
  }
  str.pb('0');
  int len = str.size() - 1;
  if(p) {
    str[len] = 'P';
    back(q - 1, p - 1, r, s, str);
  }
  if(r) {
    str[len] = 'R';
    back(q - 1, p, r - 1, s, str);
  }
  if(s) {
    str[len] = 'S';
    back(q - 1, p, r, s - 1, str);
  }
}

int n, p, r, s;
int players;

inline void main2() {
  scanf("%d %d %d %d", &n, &r, &p, &s);
  players = (1LL << n);
  verify = 0;
  ans.clear();
  back(players, p, r, s, "");
  if(verify == 0) puts("IMPOSSIBLE");
  else {
    sort(ans.begin(), ans.end());
    printf("%s\n", ans[0].c_str());
  }
}

int main() {
  int t; scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    main2();
  }
  return 0;
}