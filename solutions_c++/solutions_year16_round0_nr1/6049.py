#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int INF = 1000000000;
const int MOD = INF + 7;
const int MAXN = 100010;
const int DIGITS = (1 << 10) - 1;

int a[201];

int main(){
   freopen("A-small-attempt0.in","r",stdin);
   freopen("A-small-attempt0.out","w",stdout);
   for(int i = 1 ; i <= 200 ; i++) {
      int n = i;
      int mask = 0;
      int c = 0;
      do {
         c++;
         int aux = c * n;
         while( aux ){
            int d = aux % 10;
            aux /= 10;
            mask |= (1 << d);
         }
      } while(mask != DIGITS);
      a[i] = c * n;
   }
   int casos;
   cin >> casos;
   for(int caso = 1 ; caso <= casos ; caso++){
      int n;
      cin >> n;
      if(n == 0) {
         cout << "Case #" << caso << ": " << "INSOMNIA" << endl;
      } else {
         cout << "Case #" << caso << ": " << a[n] << endl;
      }
   }
   return 0;
}