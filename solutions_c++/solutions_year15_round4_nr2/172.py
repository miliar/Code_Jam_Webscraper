#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

struct node{
     long double tem, v;
     bool operator < (const node &A) const {
          return tem < A.tem;
     }
} a[101];
const long double eps = 1e-15;

int test, n;
long double vo, te;

bool check(long double lt) {
     long double Max = 0;
     for (int i = 1; i <= n; i++) {
          Max += lt * a[i].v;
     }
     if (Max < vo) return false;
     long double Min = 0; Max = 0;
     long double Left = vo, X = 0, Y = 0;
     for (int i = 1; i <= n; i++) {
          long double t = min(lt, Left / a[i].v);
          Left -= t * a[i].v;
          X += a[i].v * t * a[i].tem;
          Y += a[i].v * t;
          if (abs(Left) < eps) break;
     }
     Min = X / Y;
     X = 0; Y = 0; Left = vo;
     for (int i = n; i; i--) {
          long double t = min(lt, Left / a[i].v);
          Left -= t * a[i].v;
          X += a[i].v * t * a[i].tem;
          Y += a[i].v * t;
          if (abs(Left) < eps) break;
     }
     Max = X / Y;
     return Min - eps < te && te < Max + eps;
}

int main(){
     freopen("b.in", "r", stdin);
     freopen("b.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d: ", uu);
          cin >> n >> vo >> te;
          for (int i = 1; i <= n; i++) cin >> a[i].v >> a[i].tem;
          sort(a + 1, a + n + 1);
          long double Left = 0, Right = 1e10, Mid = (Left + Right) / 2;
          if (!check(Right)) {
               printf("IMPOSSIBLE\n");
               continue;
          }
          for (int i = 1; i <= 2000; i++, Mid = (Left + Right) / 2) 
               if (check(Mid)) Right = Mid;
               else Left = Mid;
          printf("%.10f\n", (double)Right);
     }
}
     
