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
    int N,M;
    scanf("%d/%d",&N,&M);

    int ans = 0;
    bool impos = false;
    if(M % 2 != 0) impos = true;
    int temp = M;

    while(temp > 1){
      if(temp % 2 != 0){
        impos = true;
      }
      temp /= 2;
    }

    while(N < M and !impos){
      N *= 2;
      ans += 1;
    }

    if(ans){
      printf("Case #%d: %d\n",i,ans);
    }else{
      printf("Case #%d: Impossible\n",i);
    }
  }
}
