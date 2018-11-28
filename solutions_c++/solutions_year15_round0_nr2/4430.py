#include<bits/stdc++.h>
using namespace std;
#define __ ios_base::sync_with_stdio(0); cin.tie(0);
#define endl '\n'
#define foreach(it, x) for (__typeof (x).begin() it = (x).begin(); it != (x).end(); ++it)
#define all(x) x.begin(),x.end()
#define D(x) cout << #x " = " << (x) << endl;

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

int dx[8] = {-1,-1,-1,0,1,1, 1, 0};
int dy[8] = {-1, 0, 1,1,1,0,-1,-1};

vector<int> toVec(int n, int s) {
  vector<int> v(s,0);
  for (int i = s - 1; n; --i) {
    v[i] = n % 10;
    n /= 10;
  }
  return v;
}

int f(int n, int t) {
  return ceil((double)n / (t + 1));
}

int mePow(int b, int p) {
  int pot = 1;
  while (p --> 0) pot *= b;
  return pot;
}

int main (){
  int TC = 1;
  int T;
  cin >> T;

  int d;
  while (T --> 0) {
    cin >> d;

    vector<int> v(d);

    for (int i = 0; i < d; ++i) cin >> v[i];

    int ans = INT_MAX;
    int lim = mePow(10,d);
    for (int i = 0; i < lim; ++i) {
      vector<int> vv = toVec(i,d);
      int tot = accumulate (all(vv),0);
      int mmax = 0;
      for (int j = 0; j < d; ++j) {
        int tmp = f (v[j], vv[j]);
        mmax = max(mmax, tmp);
      }
      tot += mmax;
      ans = min(ans, tot);
    }

    cout << "Case #" << TC ++ << ": " << ans << endl;
  }
  return 0;
}
