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
double C, F, X, cur_T, cur_C, cur_S, ans;
int main(){
    scanf("%d", &T);
    FI(i, 1, T){
          scanf("%lf%lf%lf", &C, &F, &X);
          cur_C = C, cur_T = C / 2, cur_S = 2;
          //printf("%lf %lf %lf\n", C, F, X);
          
                    // printf("%.2lf %.2lf %.2lf\n", cur_C, cur_T, cur_S);
          if(C > X - 0.00000001) ans = X / cur_S;
          else
          while(cur_C <= X - 0.000000001){
                      //printf("hi\n");
                      double left = X - cur_C;
                      
                      if(left / cur_S < X / (cur_S + F)){
                              cur_T = cur_T + left / cur_S;
                              //printf("%.2lf\n", cur_T);
                              ans = cur_T;
                              break;
                      }else{
                            cur_S += F;
                            cur_T += C / (cur_S);
                            cur_C = C;
                            ans = cur_T;
                      }
                      //printf("%.2lf %.2lf %.2lf\n", cur_C, cur_T, cur_S);
                      
          }
          printf("Case #%d: %.7lf\n", i, ans);
    }
    
    
}
