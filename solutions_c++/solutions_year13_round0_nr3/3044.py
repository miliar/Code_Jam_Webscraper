#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <cmath>

#define FOR(i,n) for(int i = 0, n_ = (n); i<n_; i++)
#define ITER(it, lst) for(typeof((lst).begin()) it = (lst).begin(); it != (lst).end(); ++it)
#define N 4

using namespace std;

inline void updatemax(int &a, int b) { if(a<b) a = b; }
inline void updatemin(int &a, int b) { if(a>b) a = b; }

bool isfair(int a){
  if(a < 0) return false;
  int b = 0, c = a;
  while(c > 0){
    b *= 10;
    b += (c%10);
    c/=10;
  }
  return a == b;
}

void collect(int A, int B, list<int> & c){
  for(int a = A; a <= B; a++) 
    if(isfair(a)) 
      if(isfair(a*a))
	c.push_back(a);
}

int floorsqrt(int a){
  int t = floor(sqrt(double(a)));
  if(t*t > a) t--;
  if((t+1)*(t+1) <= a) t++;
  return t;
}

int ceilsqrt(int a){
  int t = ceil(sqrt(double(a)));
  if(t*t < a) t++;
  if((t-1)*(t-1) >= a) t--;
  return t;
}

int main(){
  int T;
  cin>>T;
  vector<int> A(T), B(T);
  FOR(t,T) cin>>A[t]>>B[t];

  int minA = A[0], maxB = B[0];
  FOR(t,T) updatemin(minA, A[t]), updatemax(maxB, B[t]);

  list<int> fairsquares;
  collect(ceilsqrt(minA), floorsqrt(maxB), fairsquares);
 
  FOR(t,T){
    int count = 0;
    int a = ceilsqrt(A[t]), b = floorsqrt(B[t]);
    ITER(it, fairsquares) 
      if(*it>=a && *it<=b)
	count++;
    cout<<"Case #"<<t+1<<": "<<count<<endl;
  }

  return 0;
}
