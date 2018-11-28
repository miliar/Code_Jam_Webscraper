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
      int X;
      int R,C;
      scanf("%d %d %d",&X,&R,&C);
      string winner = "GABRIEL";
      if(X == 1){
	//nothing to do
      }
      else if(X == 2){
	if(R == 1 || R == 3){
	  if(C == 1 || C == 3){
	    winner = "RICHARD";
	  }
	}
      }
      else if(X == 3){
	if(R == 1 || C == 1){
	  winner = "RICHARD";
	}
	else if(R == 3 || C == 3){
	  // nothing to do
	}
	else {
	  winner = "RICHARD";
	}
      }
      else if(X == 4){
	if(R == 4 || R == 3){
	  if(C == 4 || (C == 3 && R != 3)){
	    // nothing to do
	  }
	  else{
	    winner = "RICHARD";
	  }
	}
	else{
	    winner = "RICHARD";
	}
      }

      printf("Case #%d: %s\n",test_i + 1,winner.c_str());
    }
  }
}
