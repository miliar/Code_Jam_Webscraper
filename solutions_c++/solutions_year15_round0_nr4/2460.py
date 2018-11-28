#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <math.h>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt,j,jj;
  int result;
  long grid;
  scanf("%d ", &tt);
  for(int i=0; i<tt ;++i){
    int X,R,C;
    result=0;
    scanf(" %d %d %d ",&X, &R, &C);
    grid = R*C;
    int res = X/2;
    if(X%2!=0)
    res = res+1;

    if(grid % X != 0)
      result=0;
    else if(X>C && X>R)
      result=0;
    else if(res> R || res> C)
      result =0;
    else if(X>6)
      result =0;
    else if(X==4 &&((R==2 && C==4)|| (C==2 && R==4)))
      result =0;
    else result =1;

    if (result ==0)
      cout<<"Case #"<<i+1<<": RICHARD"<<endl;
    else
      cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
  }
  return 0;
}
