#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);

  for(int i=1;i<=T;++i){
    int A,B,K;
    scanf("%d %d %d",&A,&B,&K);

    int ways = 0;

    for(int a=0;a<A;++a){
      for(int b=0;b<B;++b){
        if((a&b) < K) ++ways;
      }
    }

    printf("Case #%d: %d\n",i,ways);
  }
}
