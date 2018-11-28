#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <iomanip>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>
#include <functional>

#define pb push_back
#define mk make_pair
#define sqr(N) ((N)*(N))
#define F first
#define S second
#define maxn 101010

using namespace std;                         

typedef long long ll;
                                     
int i, j, n, t, f[5][5];

int main(){
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A-small-attempt1.out", "w", stdout);
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    scanf("%d", &n);
    for(i = 1; i <= 4; i++)
      for(j = 1; j <= 4; j++) scanf("%d", f[i] + j);
    int k[22] = {};
    for(i = 1; i <= 4; i++) k[f[n][i]]++;
    scanf("%d", &n);
    for(i = 1; i <= 4; i++)
      for(j = 1; j <= 4; j++) scanf("%d", f[i] + j);
    for(i = 1; i <= 4; i++) k[f[n][i]]++;
    int cnt = 0, ans = 0;
    for(i = 1; i <= 16; i++) if(k[i] == 2) cnt++, ans = i;
    if(cnt == 1) printf("%d\n", ans);
    else if(cnt > 1) puts("Bad magician!");
    else puts("Volunteer cheated!");
  }
  return 0;
}         