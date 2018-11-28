#include <bits/stdc++.h>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) ((int)(x).size())
#define MMS(x,n) memset(x,n,sizeof(x))
#define mms(x,n,s) memset(x,n,sizeof(x)*s)
#define pb push_back
#define mp make_pair
#define NX next_permutation
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define FIND(x,n) find(all(x),(n))-(x).begin()
#define SET_DIFF(x,y,z) set_difference(all(x) , all(y) , back_inserter(z))
#define ACC(x) accumulate(all(x),0)
#define PPC(x) __builtin_popcount(x)
#define LZ(x) __builtin_clz(x)
#define TZ(x) __builtin_ctz(x)
#define mxe(x) *max_element(all(x))
#define mne(x) *min_element(all(x))
#define low(x,i) lower_bound(all(x),i)
#define upp(x,i) upper_bound(all(x),i)
#define NXPOW2(x) (1ll << ((int)log2(x)+1))
#define PR(x) cout << #x << " = " << (x) << endl ;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef pair<int, int> pii;

const int OO = (int) 2e9;
const double eps = 1e-9;

bool vis[27];
int ret, sz;

void permute(string arr[], int p, int n) {
  int np;
  if (p == n) {
    int i, j, m;
    char ch;
    MMS(vis, 0);
    ch = arr[0][0];
    REP(i,sz)
    {
      m = SZ(arr[i]);
      REP(j,m)
        if (vis[ch - 'a'])
          goto a7a;
        else if (arr[i][j] != ch)
          vis[ch - 'a'] = 1, ch = arr[i][j];
    }
    if (!vis[ch - 'a'])
      ret++;
    a7a: ;
  } else {
    for (np = p; np <= n; np++) {
      swap(arr[p], arr[np]);
      permute(arr, p + 1, n);
      swap(arr[p], arr[np]);
    }
  }
}

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  int t, tt = 1, i, j, n, m;
  char ch;
  string arr[101], tmp, x;
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    ret = 0;
    REP(i,n)
    {
      cin >> tmp;
      MMS(vis, 0);
      ch = tmp[0];
      m = SZ(tmp);
      x = "";
      REP(j,m)
        if (vis[ch - 'a'])
          goto a7a1;
        else if (tmp[j] != ch)
          vis[ch - 'a'] = 1, x += ch, ch = tmp[j];
      if (!vis[ch - 'a'])
        x += ch;
      else
        goto a7a1;
      arr[i] = x;
    }
    sz = n;
    permute(arr, 0, n - 1);
    a7a1: ;
    printf("Case #%d: ", tt++);
    printf("%d\n", ret);
  }
  return 0;
}
