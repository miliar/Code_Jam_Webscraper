/*
   Problem:
   Author: Akai
   Date: 2012//
   Meaning£º
   Algorithm£º
*/
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int a[101][101] ;
bool vis[101][101] ;
int T , n , m;
int main(){
//	freopen("B-small-attempt1.in", "r", stdin);
 //	freopen("B-small-attempt.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
 	freopen("B-large.out", "w", stdout);
    scanf("%d" , &T);
    for (int cases = 1 ; cases <= T ; cases++){
          printf("Case #%d: " , cases);
          scanf("%d%d" , &n , &m);
          for (int i = 1 ; i <= n ; i++)
              for (int j = 1 ; j <= m ; j++) scanf("%d" , &a[i][j]);
          memset(vis , 0 ,sizeof(vis)) ;
          for (int i = 1 ; i <= n ; i++){
              int x = 0 ;
              for (int j = 1 ; j <= m ; j++) if (a[i][j] > x) x = a[i][j] ;
              for (int j = 1 ; j <= m ; j++) if (a[i][j] == x) vis[i][j] = 1 ;
          }
          for (int j = 1 ; j <= m ; j++){
              int x = 0 ;
              for (int i = 1 ; i <= n ; i++) if (a[i][j] > x) x = a[i][j] ;
              for (int i = 1 ; i <= n ; i++) if (a[i][j] == x) vis[i][j] = 1 ;
          }
          bool flag = 1;
          for (int i = 1 ; i <= n ; i++)
              for (int j = 1 ; j <= m ; j++) if (vis[i][j] != 1) flag = 0 ;
          if  (flag) puts("YES"); else puts("NO");
    }

	return 0;
}
