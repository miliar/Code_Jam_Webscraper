#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#define FI(i,a, b) for(i=a;i<=b;i++)
#define FD(i,a, b) for(i=a;i>=b;i--)
#include<map>
#define CL(x, y) memset(x, y, sizeof(x))
#define INF 100000000
#define MAXN ?
#define MAXE ?
#define x first
#define y second
#define mp make_pair
#define pi 3.1415926535
int  i, j, k ,N, M, K, T;
int map1[100][100], map2[100][100], r1[100], r2[100], c1[100], c2[100];
int main(){
    scanf("%d", &T);
    FI(i, 1, T){
          int t1, t2;
          scanf("%d", &t1);
          FI(j, 1, 4){
                FI(k, 1, 4){
                      scanf("%d", &map1[i][j]);
                      int x = map1[i][j];
                      r1[x] = j, c1[x] = k;
                }      
          }
          scanf("%d", &t2);
          FI(j, 1, 4){
                FI(k, 1, 4){
                      scanf("%d", &map2[i][j]);
                      int  x = map2[i][j];
                      r2[x] = j, c2[x] = k;
                }      
          }K =0; int ans = -1;
          for(int i = 1; i <= 16; i++){
                  if(r1[i] == t1 && r2[i] == t2){
                           K++;
                           ans = i;
                           }
          }
          if(K == 0) printf("Case #%d: Volunteer cheated!\n",  i);
          else if(K > 1) printf("Case #%d: Bad magician!\n", i);
          else printf("Case #%d: %d\n", i, ans);
    }    
}
