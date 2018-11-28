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
using namespace std;
int i, j, k, N, M, K, T;
double a[10000], b[10000];
int main(){
    scanf("%d", &T);
    FI(k, 1, T){
          scanf("%d", &N);
          FI(i, 1, N){
                scanf("%lf", &a[i]);      
          }  
          FI(i, 1, N){
                scanf("%lf", &b[i]);      
          }  
          sort(a + 1,  a + 1 + N);
          sort(b + 1, b + 1+ N);
          int maxa = 0, minb = 0;
          int l = 1, r = N;
          FI(i, 1, N){
                if(a[i] > b[l]){
                        maxa++;
                        l++;
                }else{
                      //minb++;
                }
          }
          int used[1005] ={};
          FI(i, 1, N){
                int x = 0;
                FI(j, 1, N){
                      if(used[j] == 0 && b[j] > a[i]){
                                 used[j] = 1;
                                 x = 1;
                                 break;
                      }
                }
                
          }
          
          FI(i, 1, N){
                if(used[i] == 0){
                           minb++;
                }
          }
          printf("Case #%d: %d %d\n", k, maxa, minb);
    }    
}
