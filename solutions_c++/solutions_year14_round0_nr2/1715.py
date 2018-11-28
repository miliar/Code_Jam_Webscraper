/*************************************************************************
    > File Name: b.cpp
    > Author: implus
    > Mail: 674592809@qq.com
    > Created Time: 六  4/12 12:01:36 2014
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs

int T, icase = 1;
double C, F, X;

int main(){
  scanf("%d", &T);
  while(T--){
    scanf("%lf%lf%lf", &C, &F, &X);
    int a = ceil((1.0 * F * ( X - C) - 2.0 * C) / (1.0 * F * C));
    if(a < 0) a = 0;
    double ans = 0;
    for(int i = 0; i < a; i++){
      ans += 1.0 * C / (2.0 + 1.0 * i * F);
    }
    ans += 1.0 * X / (2.0 + 1.0 * a * F);
    printf("Case #%d: %.7lf\n", icase++, ans);
  }
  return 0;
}
