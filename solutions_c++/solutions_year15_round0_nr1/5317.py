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

int main (){
  int TC = 1;
  int T;
  cin >> T;

  int a;
  string b;
  while (T --> 0) {
    cin >> a >> b;

    int ans = 0;
    int ind = 0;
    int sum = 0;

    while (ind < a) {
      while (b[ind] == '0' && ind < a) {
        ans ++;
        sum ++;
        ind ++;
      }

      while (b[ind] != '0' && ind < a) {
        sum += toInt(b[ind]);
        ind ++;
      }

      while (ind < sum) {
        sum += toInt(b[ind]);
        ind ++;
      }
      ind = sum;
    }

    cout << "Case #" << TC ++ << ": " << ans << endl;
  }

  return 0;
}
