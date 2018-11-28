#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define st first
#define nd second
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<
 
const int oo = 0x3f3f3f3f;
 
typedef long long ll;
typedef pair<int,int> pii;

int main() {
  int T;
  cin >> T;
  fr(caso,1,T+1) {
    string S;
    cin >> S;
    
    string ans = "";
    for (char c : S) {
      if (ans == "") ans = string(1, c);
      else if (c >= ans[0]) ans = string(1, c) + ans;
      else ans += c;
    }
    
    
    printf("Case #%d: %s\n", caso, ans.c_str());
  }
  
  return 0;
}