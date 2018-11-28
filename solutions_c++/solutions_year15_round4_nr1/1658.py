#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;

const int MAXN = 101*101;

int R, C;

int dr[4] = {0 , 0, 1,-1};
int dc[4] = {1 ,-1, 0, 0};

map<char, int> direction = {
   {'<', 1},
   {'>', 0},
   {'^', 3},
   {'v', 2}
};

vector<int> adj[MAXN];

int main(){
#ifndef ONLINE_JUDGE
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
#endif
   char arrow[4] = {'<','>','^','v'};
   int casos;
   cin >> casos;
   for(int caso = 1 ; caso <= casos ; caso++){
      cin >> R >> C;

      for(int i = 0 ; i < R*C ; i++ ){
         adj[i].clear();
      }

      bool possible = true;

      vector<string> s(R);

      for(int i = 0 ; i < R ; i++){
         cin >> s[i];
      }
      int ans = 0;

      for(int i = 0 ; i < R ; i++){
         for(int j = 0 ; j < C ; j++){
            if(s[i][j] != '.') {
               int r = 0;
               for(int k = 0 ; k < R ; k++){
                  r += s[k][j] != '.'; 
               }
               int c = 0;
               for(int k = 0 ; k < C ; k++){
                  c += s[i][k] != '.'; 
               }
               if(r == 1 && c == 1) {
                  possible = false;
               }
               int d = direction[s[i][j]];
               r = i, c = j;
               bool sw = false;
               while( r < R && c < C && r >= 0 && c >= 0 ){
                  if((r != i || c != j) && s[r][c] != '.') {
                     sw = true;
                     break;
                  }
                  r = r + dr[d];
                  c = c + dc[d];
               }
               if(!sw) {
                  ans++;
               }
            }
         }
      }


      cout << "Case #" << caso << ": ";
      if(possible) {
         cout << ans << endl;
      } else {
         cout << "IMPOSSIBLE" << endl;
      }
   }
   return 0;
}