//Javier Guzmán
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int t;
ll k, c, s;

int main(){
   scanf("%d", &t);
   for(int test=1; test<=t; test++){
      scanf("%lld%lld%lld", &k, &c, &s);
      printf("Case #%d:", test);
      ll l=1;
      for(ll i=1; i<c; i++){
         l*=k;
      }
      for(ll i=1; i<=l*k; i+=l){
         printf(" %lld", i);
      }
      printf("\n");
   }
   return 0;
}
