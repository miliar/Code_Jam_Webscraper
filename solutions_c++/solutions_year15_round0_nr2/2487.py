#define _USE_MATH_DEFINES
#define INF 0x3f3f3f3f
#include <cstdio>
#include <iostream>
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
#include <iterator>
#include <complex>
#include <assert.h>
 
using namespace std;
 
typedef long long ll;
typedef pair <double,double> P;
typedef pair <int,P > PP;
 
int tx[] = {+0,+1,+0,-1};//URDL
int ty[] = {-1,+0,+1,+0};
 
static const double EPS = 1e-8;

int main(){
  int num_of_testcases;
  while(~scanf("%d",&num_of_testcases)){
    for(int test_i = 0; test_i < num_of_testcases; test_i++){
      int num_of_diners;
      scanf("%d",&num_of_diners);
      vector<int> diners;

      int max_pancakes = 0;
      int cost = INF;
      for(int i = 0; i < num_of_diners; i++){
	int num_of_pancakes;
	scanf("%d",&num_of_pancakes);
	diners.push_back(num_of_pancakes);
	max_pancakes = max(max_pancakes,num_of_pancakes);
      }

      for(int i = 1; i <= max_pancakes; i++){
	int sum = i;
	for(int diner_i = 0; diner_i < diners.size(); diner_i++){
	  if(diners[diner_i] > i){
	    sum += diners[diner_i] / i 
	      - (diners[diner_i] % i == 0 ? 1 : 0);
	  }
	}
	cost = min(cost,sum);
      }
      printf("Case #%d: %d\n",test_i + 1,cost);
    }
  }
}
