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
 
using namespace std;
 
typedef long long ll;
typedef pair <int,int> P;
typedef pair <int,P > PP;
 
const int tx[] = {0,1,0,-1};
const int ty[] = {-1,0,1,0};

bool FindHigherGrassInCol(int stage[101][101],int H,int x,int my_h){
  for(int y=0;y<H;y++){
    if(stage[y][x] > my_h) return true;
  }
  return false;
}

bool FindHigherGrassInRow(int stage[101][101],int W,int y,int my_h){
  for(int x=0;x<W;x++){
    if(stage[y][x] > my_h) return true;
  }
  return false;
}

int main(){
  int H,W;
  int T;
  while(~scanf("%d",&T)){
    for(int test_num = 0; test_num < T; test_num++){
      scanf("%d %d",&H,&W);
      int stage[101][101];
      for(int y=0;y<H;y++){
	for(int x=0;x<W;x++){
	  scanf("%d",&stage[y][x]);
	}
      }

      bool isok = true;
      for(int y=0;y<H;y++){
	for(int x=0;x<W;x++){
	  int height = stage[y][x];
	  if(FindHigherGrassInCol(stage,H,x,height)
	     && FindHigherGrassInRow(stage,W,y,height)){
	    isok = false;
	    goto found;
	  }
	}
      }
    found:;
      printf("Case #%d: %s\n",test_num+1,isok ? "YES" : "NO");
    }
  }
}
