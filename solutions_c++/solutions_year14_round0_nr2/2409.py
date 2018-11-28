#define _USE_MATH_DEFINES
#define INF 0x3f3f3f3f

#include <iostream>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>
#include <cctype>
#include <utility>
  
using namespace std;
  
typedef long long ll;
typedef pair <int,int> P;
typedef pair <int,P> PP;
  
static const double EPS = 1e-8;
  
static const int tx[] = {0,1,0,-1};
static const int ty[] = {-1,0,1,0};

double dp[101][10001];

int main(){
  int T;
  scanf("%d",&T);
  for(int test_idx=1;test_idx<=T;test_idx++){
    double farm,add_speed,goal;
    scanf("%lf %lf %lf",&farm,&add_speed,&goal);
    double speed = 2.0;
    double current = 0;

    while(1){
      double farm_cost = farm / speed;
      //use farm 
      double use_cost = goal / (speed + add_speed) + farm_cost;

      //un-use farm
      double  unuse_cost = goal / speed;

      if(use_cost < unuse_cost){
	speed += add_speed;
	current += farm_cost;
      }
      else{
	current += unuse_cost;
	break;
      }
    }

    printf("Case #%d: %.7lf\n",test_idx,current);
  }
}
