#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;
long long t,pp,i,j,s,f,x,k,l,m,n,a,b,c,d,e,u;
int main() {
  cin>> t;
  while (t --){
      e ++;
      s = 0;
      cin >>a>>b>>k;
      s = 0;
      for (i = 0; i < a; i ++){
          for (j = 0; j< b; j ++){
              if ((i&j) < k)s ++;
          }
      }
      cout << "Case #"<<e<<": "<< s<<endl;
  }
  return 0;
}
