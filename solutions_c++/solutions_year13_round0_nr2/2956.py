#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
const int inf = 1<<29;
const int maxn = 123;
int N , M , g[maxn][maxn] , cas;
vector<int> li;
void input() {
     cin >> N >> M;
     set<int> s;
     set<int> :: iterator it;
     memset(g,0 ,sizeof(g));
     for(int i = 1; i <= N ; i++) {
         for(int j = 1; j <=M; j++) {
             cin >> g[i][j];
             s.insert(g[i][j]);
         }
     }
     li.clear();
     for(it = s.begin() ;it != s.end(); it++) {
         li.push_back(*it); 
     }
}
bool judge(int now) {
     bool used[maxn][maxn], ok;
     memset(used, false , sizeof(used));
     for(int i = 1; i <= N ; i++) {
         ok = true;
         for(int j = 1 ; j <=M ; j++) {
             if(g[i][j] > now) {
                  ok = false;
                  break;
             }
         }
             
         if(ok) {
            for(int j = 1 ; j <=M ; j++) {
               if(g[i][j] == now) {
                  used[i][j] = true;
               }
            }                   
         }
     }
         
      for(int i = 1; i <= M ; i++) {
          ok = true;
          
          for(int j = 1 ; j <=N ; j++) {
              if(g[j][i] > now) {
                   ok = false;
                   break;
              }
          }
             
          if(ok) {
              for(int j = 1 ; j <=N ; j++) {
                 if(g[j][i] == now) {
                    used[j][i] = true;
                 }
              }                   
          }
      }
         
      for(int i = 1; i <= N ; i++) {
          for(int j = 1 ; j <=M ; j++) {
              if((g[i][j] == now) && !used[i][j]) {
                          return false;
              }            
          }
      }
     
     return true;
}

void solve() {
     bool flag = true;
     cout << "Case #"<<cas <<": ";
     for(int i =li.size()-1; i >=0; i--) {
        if (!judge(li[i])) {
            cout << "NO" << endl;
            return ;
        }
     }
     cout << "YES" << endl;
     return;
}

int main() {
    int T ;
    freopen("C:/Users/wangkun/Downloads/B-large.in", "r" , stdin);
    freopen( "D:/result.out",  "w",stdout); 

    cas  = 0;
    cin >> T;
    while(T--) {
         cas ++;
         input();
         solve();
    }
}
