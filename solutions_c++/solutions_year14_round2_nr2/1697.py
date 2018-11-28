#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;

int main(){
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small-attempt0.out", "w", stdout);
   
   int testn;
   cin >> testn;
   
   
   
   
   
   for(int test = 1; test <= testn; test++){
      unsigned int a, b, k;
      cin >> a >> b >> k;
      
      int sum = 0;
      for(unsigned int i = 0; i < a; ++i){
      for(unsigned int j = 0; j < b; ++j){
         if( (i & j) < k ) sum++;
      }}
      
      printf("Case #%d: %d\n", test, sum);
   }
   
   return 0;
}
