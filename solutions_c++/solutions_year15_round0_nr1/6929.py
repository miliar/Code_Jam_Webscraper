#include<bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i, a, b) for(int i = (a); i <= (b); i++)
#define fd(i, a, b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int, int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int, int> >
#define MOD 1000000007
#define ODD(x) (x & 1)
#define ones(x) __builtin_popcount(x)
#define CLX(x, y) memset(x, y, sizeof(x))

int main(){
  int t, i, j, n, k;
  int p, ans;
  string s;
  cin >> t;
  f(i, 1, t){
    p = 0;
    ans = 0;
    cin >> n >> s;
    f(j, 0, n){
      p += (int)(s[j]-'0');
      if(p>j) continue;
      else{
        ans += (p-j+1);
        p += (p-j+1);
      }
    }
    cout << "Case #" << i << ": " << ans << "\n";
  }
  return 0;
}
