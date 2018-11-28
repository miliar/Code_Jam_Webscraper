#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <functional>
#include <bitset>
#include <deque>
#include <tuple>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int, int> pii;

#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define FORD(i, x, y) for (ll i = x; i >= y; --i)
#define REP(i, n) for(ll i=0; i<n; i++)
#define REPD(i, n) for(ll i = n - 1; i >= 0; --i) 

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQ(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SZ(c) (int)(c).size()
#define CONTAINS(s,obj) (s.find(obj)!=s.end())

#define CLEAR(x) memset(x,0,sizeof x)
#define COPY(from,to) memcpy(to, from, sizeof to)

#define sq(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second

const double eps = 1.0e-11;
const double pi = acos(-1.0);

struct Node {
  unordered_map<char, Node*> p;
  bool ed;
  Node() {}
};

void Insert(Node* root, const string& s) {
  // if (rand() % 10000 == 0) cerr << "Inserting: " << s << endl;
  for (int i = 0; i < s.size(); ++i) {
    if (!root->p.count(s[i])) root->p[s[i]] = new Node();
    root = root->p[s[i]];
  }
  root->ed = true;
}

Node* Build(const vector<string>& dict) {
  Node* root = new Node();
  for (const string& s : dict) Insert(root, s);
  return root;
}


int res;

void Rec(Node* r) {
  ++res;
  for(auto x : r->p) Rec(x.second);
  delete r;
}

int Count(vector<string> vs) {
  auto root = Build(vs);
  res = 0;
  Rec(root);
  return res;
}

vector<string> d;
vector<int> col;
set<string> uniq;
int mx, cnt;
int n, m;

void Get() {
  string x;
  REP(i, SZ(col)) x += '0' + col[i];
  if (CONTAINS(uniq, x)) return;
  uniq.insert(x);
  int tmp = 0;
  REP(i, 4) {
    vector<string> curr;
    REP(j, SZ(col)) if (col[j] == i) curr.push_back(d[j]);
    if (curr.empty()) continue;
    tmp += Count(curr);
  }
  if (tmp == mx) ++cnt;
  if (tmp > mx) mx = tmp, cnt = 1;
}

void GetOther(int pos) {
  if (pos == SZ(col)) {
    Get();
    return;
  }
  if (col[pos] != -1) GetOther(pos + 1);
  else {
    REP(i, m) {
      col[pos] = i;
      GetOther(pos + 1);
      col[pos] = -1;
    }
  }
}

void GetOne(int gr) {
  if (gr == m) {
    GetOther(0);
    return;
  }
  REP(i, SZ(col)) {
    if (col[i] == -1) {
      col[i] = gr;
      GetOne(gr + 1);
      col[i] = -1;
    }
  }
}

// Need an endl after output.
void solve() {  
  cin >> n >> m;
  d.resize(n), col.assign(n, -1);
  REP(i, n) cin >> d[i];
  if (m == 1) {
    cout << Count(d) << " 1\n";
    return;
  }
  uniq.clear();
  /*if (n == m) {
    int tmp = 0;
    REP(i, n) {
      vector<string> curr;
      curr.push_back(d[i]);
      tmp += Count(curr);
    }
    cout << tmp << " " << 1 << endl;
    return;
  }*/
  mx = 0, cnt = 0;
  GetOne(0);  
  cout << mx << " " << cnt << endl;
}

int main() {
  freopen("D-small-attempt1.in", "r", stdin);
  freopen("d.out", "w", stdout);
  int tests;
  scanf("%d", &tests);
  REP(i, tests) {
    cerr << i << endl;
    printf("Case #%d: ", int(i + 1));
    solve();
  }
  return 0;
}