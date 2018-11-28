#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#define DEBUG printf("TEST\n")

using namespace std;

const long long MAX = 10000000;
long long a, b, i;
int cum[10000005];

long long inv(long long num){
   long long ret = 0;
   while(num > 0){
      ret = ret * 10 + (num % 10);
      num /= 10;
   }
   return ret;
}

bool chksqr(long long num){
   return ((long long) sqrt(num)) * ((long long) sqrt(num)) == num;
}

bool chkpal(long long num){
   return num == inv(num);
}

bool chknum(long long num){
   return chkpal(num) && chksqr(num) && chkpal((int) sqrt(num));
}

int main(){
   
   for(i = 1; i <= MAX; ++i){
      cum[i] = cum[i - 1];
      if(chknum(i * i)) cum[i] += 1;
   }
   
   int TC, itc;
   scanf("%d", &TC);
   for(itc = 1; itc <= TC; ++itc){
      scanf("%lld %lld", &a, &b);
      printf("Case #%d: ", itc);
      
      if(chksqr(a)){
         printf("%d\n", cum[(int) sqrt(b)] - cum[(int) sqrt(a) - 1]);
      }
      else{
         printf("%d\n", cum[(int) sqrt(b)] - cum[(int) sqrt(a)]);
      }
   }
   
   return 0;
}
