/*
 * Author:  Yzcstc
 * Created Time:  2014/4/12 21:21:29
 * File Name: A.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<ctime>
#include<utility>
#define M0(x) memset(x, 0, sizeof(x))
#define MP make_pair
#define Fi first
#define Se second
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define PB push_back
#define Inf 0x3fffffff
#define eps 1e-8
typedef long long LL;
using namespace std;
int vis[17], n;

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    int r_1, r_2, x;
    for (int i = 1; i <= cas; ++i){
         scanf("%d", &r_1);
         M0(vis);
         for (int j = 0; j < 4; ++j)
              for (int k = 0; k < 4; ++k){
                  scanf("%d", &x);
                  if (j == r_1-1) vis[x] = 1;
              }
         int cnt = 0;
         scanf("%d", &r_2);
         int last = 0;
         for (int j = 0; j < 4; ++j)
              for (int k = 0; k < 4; ++k){
                  scanf("%d", &x);
                  if (j == r_2-1 && vis[x]) ++cnt, last = x;
              }
         if (cnt == 1) printf("Case #%d: %d\n",i,  last);
         else if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", i);
         else printf("Case #%d: Bad magician!\n", i);
                  
    }
    fclose(stdin);  fclose(stdout);
    return 0;
}
