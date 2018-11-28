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
ll n, k, ans;
set<int> digits;
int main(){
   scanf("%d", &t);
   for(int test=1; test<=t; test++){
      digits.clear();
      scanf("%lld", &n);
      if(n==0){
         printf("Case #%d: INSOMNIA\n", test);
         continue;
      }
      ans=0;
      while(digits.size()<10){
         ans+=n;
         k=ans;
         while(k){
            digits.insert(k%10);
            k/=10;
         }
      }
      printf("Case #%d: %lld\n", test, ans);
   }
   return 0;
}
