
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
//#define LOCAL
using namespace std;
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define clean(n,val) memset((n),(val),sizeof(n))
#define MP make_pair
#define PB push_back
#define ll long long
#define debug(x) x
typedef pair<int, int> PI;
const int INF = 0xFFFFFFF;
const int MOD = 1e9+7;
const int MAXN = 100005;




int main() {
  int T, kase = 1;
  #ifdef LOCAL
    freopen("input2.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
  #endif
  cin >> T;
  int n;
  while ( T-- ) {
    vector<int> st;
    int calc[2505] = {0};
    cin >> n;
    for ( int i = 0 ; i < 2*n-1 ; i++ ) {
      for ( int j = 0 ; j < n ; j++ ) {
        int a;
        cin >> a;
        calc[a]++;
      }
    }

    cout << "Case #" << kase << ":";
    for ( int i = 0 ; i < 2501 ; i++ ) if ( calc[i] % 2 == 1 ) cout << " " << i;
      kase++;cout << endl;
  }

  return 0;
}
