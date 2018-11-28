#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int INF = 1000000000;
const int MOD = INF + 7;
const int MAXN = 100010;

int main(){
#ifndef ONLINE_JUDGE
   freopen("in","r",stdin);
#endif
   
   int casos;
   cin >> casos;
   for(int caso = 1 ; caso <= casos ; caso++){
      int n, k, c = 0;
      cin >> n >> k;
      vector<vector<int>> jams;
      for(int mask = 0 ; mask < (1 << (n-2)) && c < k ; mask++) {
         int m = (1 << (n-1)) | 1 | (mask << 1);
         vector<int> jam;
         jam.push_back(m);
         bool is_jam = true;
         for(int base = 2 ; base <= 10 && is_jam ; base++) {
            ll b = 1, x = 0;
            for(int i = 0 ; i < n ; i++){
               if(m & (1 << i)) {
                  x += b;
               }
               b *= base;
            }
            int l = -1;
            bool is_prime = true;
            for(ll i = 2 ; i * i <= x ; i++) {
               if(x % i == 0) {
                  l = i;
                  is_prime = false;
                  break;
               }
            }
            jam.push_back(l);
            is_jam &= !is_prime;
         }
         if(is_jam) {
            c++;
            jams.push_back(jam);
         }
      }
      cout << "Case #" << caso << ":" << endl;
      for(int i = 0 ; i < jams.size() ; i++) {
         for(int j = n-1 ; j >= 0 ; j--){
            cout << ((jams[i][0] & (1 << j)) ? 1 : 0);
         }
         for(int j = 1 ; j < 10 ; j++){
            cout << " " << jams[i][j];
         }
         cout << endl;
      }

   }

   return 0;
}