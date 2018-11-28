#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <limits.h>
#include <string>
#include <string.h>
#include <sstream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

typedef long long ll;

double solver( double c, double f, double x ){
  double speed = 2.0;
  double time = 0.0;
  double finish_time = x / speed;
  
  if( finish_time <= c ){
    return finish_time;
  }

  while(true){
    finish_time = x / speed + time;
    time += c / speed;
    speed += f;

    if( time + x / speed >= finish_time ){
      return finish_time;
    }
  }

  return finish_time;
}

int main(){
  int test_case;
  double c, f, x;
  cin >> test_case;

  for(int i = 1; i <= test_case; i++){
    cin >> c >> f >> x;
    printf("Case #%d: %0.7f\n", i, solver( c, f, x ) );
  }
  return 0;
}
