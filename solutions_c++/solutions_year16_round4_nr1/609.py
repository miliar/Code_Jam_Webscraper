#include <bits/stdc++.h>

#define fori(i,b,e) for (int i = (b); i < (e); i++)
#define mp make_pair
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define elsif else if
#define sz(a) ((int)(a).size())
#define X first
#define Y second

using namespace std;

typedef long long int int64;
typedef pair<int, int> pii;
typedef vector<int> vi;

inline int getInt() { int res;  scanf("%d", &res);  return res; }
inline double getDbl() { double res;  scanf("%lf", &res);  return res; }

int cnt[3];
int res[1 << 12];
char chars[3] = {'P', 'R', 'S'};

// P=0, R=1, S=2

inline int select(int a, int b) {
  if (a > b)
    swap(a, b);
  if (a == 0 && b == 1)
    return 0;
  if (a == 1 && b == 2)
    return 1;
  assert(a == 0 && b == 2);
  return 2;
}

bool check(int n) {
  vector<int> a;
  fori(i,0,n) {
    a.pb(res[i]);
  }
  while (sz(a) > 1) {
    vector<int> b;
    for (int i = 0; i < sz(a); i += 2) {
      if (a[i] == a[i+1])
        return false;
      b.pb(select(a[i], a[i+1]));
    }
    a = move(b);
  }
  return true;
}

void print(int n) {
  fori(i,0,n) {
    printf("%c", chars[res[i]]);
  }
  printf("\n");
}

int64 code(int i, int j, int k) {
  int64 res = 0;
  res = (res << 13) + i;
  res = (res << 13) + j;
  res = (res << 13) + k;
  return res;
}

map<int64, string> m;

string get(int i, int j, int k) {
  int d =  (i + j + k) / 3;
  assert(i == d || i == d+1);
  assert(j == d || j == d+1);
  assert(j == d || j == d+1);
  int key = code(i,j,k);
  auto p = m.find(key);
  if (p != m.end())
    return p->Y;
  int sum = (i + j + k);
  if (sum == 2) {
    string res = "aa";
    res[0] = i == 1 ? 'P' : 'R';
    res[1] = k == 1 ? 'S' : 'R';
    return m[key] = res;
  }
  int half = sum / 2;
  int i1 = (i+1) / 2;
  int k1 = k / 2;
  int j1 = half - i1 - k1;
  string res = get(i1,j1,k1) + get(i-i1, j-j1, k-k1);
  return m[key] = res;
}

void solve() {
  int n = getInt();
  int sum = 0;
  fori(i,0,3) {
    cnt[i] = getInt();
    sum += cnt[i];
  }
  swap(cnt[0], cnt[1]);
  int d = sum / 3;
  fori(i,0,3) {
    if (cnt[i] != d && cnt[i] != d+1) {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  string resStr = get(cnt[0], cnt[1], cnt[2]);
  fori(i,0,sum) {
    res[i] = resStr[i] == 'P' ? 0 : resStr[i] == 'R' ? 1 : 2;
  }
  assert(check(sum));
  cout << get(cnt[0], cnt[1], cnt[2]) << endl;
}

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  srand(time(0));

  int N = getInt();
  fori(T,1,N+1) {
    printf("Case #%d: ", T);
    solve();
  }
  return 0;
}
