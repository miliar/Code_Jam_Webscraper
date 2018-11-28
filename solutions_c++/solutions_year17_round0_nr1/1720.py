#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef long long ll;

#define fi first
#define se second
#define pb push_back
#define rep(i, a, b) for(int (i)=(a); (i)<(b); (i)++)

const int INF = 0x3f3f3f3f;


int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  int n, x;
  string s;
  cin >> n;
  rep(kase, 1, n+1){
    cin >> s >> x;
    int res = 0, poss = 1;
    for (int i=0; i<=s.length()-x; i++){
      if (s[i] == '+'){
        continue;
      }else{
        rep(j, i, i+x){
          s[j] = (s[j] == '+'? '-' : '+');
        }
        res++;
      }
      // cout << s << endl;
    }
    rep(j, 0, s.length()){
      if (s[j] == '-'){
        cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
        poss = 0;
        break;
      }
    }
    if (poss){
      cout << "Case #" << kase << ": " << res << endl;
    }
  }
  return 0;
  
}  
