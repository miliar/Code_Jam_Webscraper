#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>

using namespace std;

bool full(vector<int> possible, int V) {
   for(int i = 1; i <= V; i++)
      if(possible[i] != 1) return false;
   return true;
}

int main() {
   int T, C, D, V;
   int temp, sum, ans;
   scanf("%d", &T);
for(int kase = 1; kase <= T; ++kase) {
   scanf("%d %d %d", &C, &D, &V);
   vector<int> denominator;
   vector<int> possible(1000,0);
   possible[0] = 1;
   ans = 0;
   for(int i = 0; i < D; i++) {
      scanf("%d", &temp);
      denominator.push_back(temp);
      possible[temp] = 1;
   }
   for(int mask = 0; mask < (1<<D); mask++) {
      sum = 0;
      for(int i = 0; i < D; i++) {
         if(mask & (1<<i)) {
            sum += denominator[i];
         }
      }
      possible[sum] = 1;
   }
   while(!full(possible,V)) {
      ans += 1;
      for(int i = 1; i <= V; i++)
         if(possible[i] != 1) {
            denominator.push_back(i);
            break;
         }
      D += 1;
      for(long long int mask = 0LL; mask < (1LL<<D); mask++) {
         sum = 0;
         for(long long int i = 0; i < D; i++) {
            if(mask & (1<<i)) {
               sum += denominator[i];
            }
         }
         possible[sum] = 1;
      }
   }
   printf("Case #%d: %d\n", kase, ans);
}
   return 0;
}
