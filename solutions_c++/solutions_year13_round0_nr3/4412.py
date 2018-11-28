#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#define INF 1000000000000LL

typedef long long int64;
typedef unsigned long long qword;
using namespace std;

/* Problem: Google Code Jam Qualification Round 2013
 *          Problem C. Fair and Square
 * URL: https://code.google.com/codejam/contest/2270488/dashboard#s=p2
 */

bool checkpalin(int64 x) {
   int digit[200];
   int n;
   n=0;
   while (x>0) {
      n++;
      digit[n] = x%10;
      x = x/10;
   }
   bool palin = true;
   for (int m=1; m<=n; m++) {
      if (digit[n-m+1] != digit[m]) {
         palin = false;
      }
   }
   return palin;
}

int main() {
   int s,t;
   int64 a,b;
   int64 ans;
   int64 i,j;
   int64 minsq,maxsq;
   cin>>t;
   for (s=1; s<=t; s++) {
      cin>>a;
      cin>>b;
      minsq = int(floor(sqrt(a)));
      maxsq = int(floor(sqrt(b))+1);
      ans = 0;
      for (i=minsq; i<=maxsq; i++) {
         if (checkpalin(i)){
            j=i*i;
            if ((j>=a) && (j<=b)) {
               if (checkpalin(i*i)) {
                  ans++;
               }
            }
         }
      }
      cout<<"Case #"<<s<<": ";
      cout<<ans<<endl;
   }
   return 0;
}
