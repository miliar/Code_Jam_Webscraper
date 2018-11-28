#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <limits>
#include <functional>

using namespace std;

#define INF (numeric_limits<long long>::max() - 1)

double pi = 3.14159265359;
int T;
long double sqr(long x){
  return x * x;
} 
int main(){
  freopen("input.txt", "r", stdin);
  cin>>T;
  for(int times = 0; times < T; ++times){
    long long r, res;
    long double t;
    res = 0;
    cin>>r>>t;
    for(;t >= 0;r+=2){
      double white = sqr(r);
      double black = sqr(r + 1);
      if(t - (black - white) < 0)break;
      else {
	t -= (black - white);
	res++;
      }
    }
    cout<<"Case #"<<times + 1<<": "<<res<<endl;
  }
  return 0;
}
