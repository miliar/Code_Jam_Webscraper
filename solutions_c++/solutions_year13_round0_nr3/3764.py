#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>
#include <climits>
#include <functional>


#include "../bigint/BigIntegerLibrary.hh"

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back


typedef unsigned int uint;
typedef long long LL;
typedef long double LD;

typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl

#include <chrono>


bool palindrome(int num)
{
   int numc = num;
   int digit, rev = 0;
   do
   {
      digit = num%10;
      rev = (rev*10) + digit;
      num = num/10;
   } while (num!=0);
   return (rev == numc);
}

int main(int argc, char **argv)
{

   int testcases, small, big, cont;


   cin >> testcases;

   for (int caso = 1; caso <= testcases; ++caso)
   {
      cin >> small;cin >> big; 

      cont = 0;
      for (int i = small; i <= big; i++) {
         if (palindrome(i)) {
            float f = sqrtf(float(i));
            if (int(f) == f && palindrome((int)f)) {
               cont++;
               //cout << i << " ";
            }
            
         }
      }
      cout << "Case #" << caso << ": " << cont <<  endl;
      
   }

}