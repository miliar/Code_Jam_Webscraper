#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

long long t,pp,i,j,a,b;
vector <long long> p,q;
double s,f,x,k,l,m,n,c;
int main() {
  cin >>t;
  while (t --){
  	cin >> c>>f>>x;
    s = 111111111111.0;
    a = 100000;
    m = 0.0;
    n = 2.0;
    while (a --){
      if (s > m + x / n) s = m+ x / n;
      m += c / n;
      n += f;
    }
    printf ("Case #%lld: %.7lf\n",++pp,s);
 //   cout << endl;
  }
  
  return 0;
}
