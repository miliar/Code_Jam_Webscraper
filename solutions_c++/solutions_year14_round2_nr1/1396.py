#include <bits/stdc++.h>

using namespace std;

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

int n, ret;
int idx[101];
int cnt[101];
string arr[101];

bool valid() {
  int i, j, res;
  char ch;
  MMS(idx, 0);
  while (true) {
    ch = arr[0][idx[0]];
    REP(i,n)
    {
      res = 0;
      rep(j,idx[i],SZ(arr[i]))
      {
        if (arr[i][j] != ch)
          break;
        res++;
      }
      if (!res)
        return 0;
      cnt[i] = res;
      idx[i] = j;
    }
    bool isEnd = 0, wrong = 0;
    int r1 = OO, r2;
    REP(i,n)
    {
      if (idx[i] == SZ(arr[i]))
        isEnd = 1;
      else
        wrong = 1;
      r2 = 0;
      REP(j,n)
        if (i != j)
          r2 += abs(cnt[i] - cnt[j]);
      r1 = min(r1, r2);
    }
    ret += r1;
    if (isEnd)
      return !wrong;
  }
  return 1;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  int i, t, tt = 1;
  cin >> t;
  while (t--) {
    cin >> n;
    ret = 0;
    printf("Case #%d: ", tt++);
    REP(i,n)
      cin >> arr[i];
    if (!valid())
      puts("Fegla Won");
    else {
      printf("%d\n", ret);
    }
  }
  return 0;
}
