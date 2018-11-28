#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <string.h>
#include <sstream>
#include <set>
using namespace std;
#define MAXN  200
#define INF  1000000000
#define pb push_back
typedef long long ll;
int N , M ;
string brd[MAXN];
int dxx[] = {0 ,0 , 1,-1, 1 , 1 , -1 ,-1};
int dyy[] = {1 ,-1, 0, 0, 1 ,-1 , 1  ,-1};
int a[MAXN][MAXN] , b[MAXN][MAXN];
bool exist[ MAXN ];
vector<int> nums;
bool possible (int v , int u , int n , int dx , int dy) {
     int x = v , y = u;
     while ( x < N && y < M && x >= 0 && y >= 0) {
           if (a[x][y] > n ) return false;
           x = x + dx;
           y = y + dy;
     }
     return true;
}
void execute(int v , int u , int n , int dx , int dy) {
     int x = v , y = u;
     while ( x < N && y < M&& x >= 0 && y >= 0) {
           b[x][y] = n;
           x = x + dx;
           y = y + dy;
     }
}
string calc () {
     for (int i = 1; i < nums.size(); i ++ ) {
          for (int v = 0; v < N; v ++ ) {
               if ( possible (v , 0 , nums[i] , 0 , 1 ) ) {
                    execute  (v , 0 , nums[i] , 0 , 1);         
               }  
          }
          for (int u = 0; u < M; u ++ ) {
               if ( possible (0 , u , nums[i] , 1 , 0 ) ) {
                    execute  (0 , u , nums[i] , 1 , 0);         
               }  
          }
     }
     for (int i = 0; i < N; i ++ )
         for (int j = 0; j < M; j ++ )
             if (b[i][j] != a[i][j]) return "NO";
     return "YES";              
}
int main(){  
    freopen ("B-large.in" , "r" , stdin);
    freopen ("out.txt" , "w" , stdout);
    int T; cin >> T; int t = 1;
    while (T--) {
    cin >> N >> M;
    memset (exist , 0 , sizeof (exist) );
    for (int i = 0; i < N; i ++ )
        for (int j = 0; j < M; j ++ ) {
             scanf("%d",&a[i][j]);
             if ( exist[a[i][j]] ) continue;
             nums.pb (a[i][j]); exist[a[i][j]] = 1;
        }
    sort (nums.rbegin() , nums.rend() );
    for (int i = 0; i < N; i ++) for (int j = 0; j < M; j ++ ) b[i][j] = nums[0];
    cout <<"Case #"<<t<<": "<<calc () << endl; t++;
    }  
//system("pause");              
return 0;
}

