#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<complex>
#include<numeric>
#include<set>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<utility>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<climits>
#include<cfloat>
#include<cassert>

using namespace std;

typedef unsigned long long LL;

int main(){
  int T;
  cin>>T;
  for(int C=1;C<=T;C++){
    LL r,t,count=0;
    cin>>r>>t;
    while(true){
      if(t<2*r+1)break;
      count++;
      t-=2*r+1;
      r+=2;
    }
    printf("Case #%d: %lld\n",C,count);
  }
  return 0;
}