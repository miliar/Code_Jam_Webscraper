#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int INF = 1000000000;
const int MOD = INF + 7;
const int MAXN = 100010;

int main(){

   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   
   int casos;
   cin >> casos;
   for(int caso = 1 ; caso <= casos ; caso++){
      string s;
      cin >> s;
      int n = s.size();
      int k = 1;
      char c = s[0];
      for(int i = 0 ; i < n ; i++) {
         if(c != s[i]) {
            k++;
         }
         c = s[i];
      }
      int ans;
      if(s[n-1] == '+') {
         ans = k-1;
      } else {
         ans = k;
      }
      cout << "Case #" << caso << ": " << ans << endl;
   }
   return 0;
}