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

int i, t;

int main(){
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    double c, f, x, best = 1e15, cur = 2, alltime = 0;
    scanf("%lf %lf %lf", &c, &f, &x);
    for(i = 1; i <= x; i++) {
      double times = x / cur;
      best = min(best, alltime + times);
      alltime += c / cur;
      cur += f;
    }
    printf("%.7lf\n", best);
  }
  return 0;
}         