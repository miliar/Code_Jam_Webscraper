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

int main(){
  int T;
  while(~scanf("%d",&T)){
    for(int test_idx=1;test_idx<=T;test_idx++){
      int candidates[20];
      int stage[4][4];
      memset(candidates,0,sizeof(candidates));

      for(int i=0;i<2;i++){
	int row;
	scanf("%d",&row);
	for(int y=0;y<4;y++){
	  for(int x=0;x<4;x++){
	    int card;
	    scanf("%d",&card);
	    stage[y][x] = card;
	  }
	}
	
	int y=row-1;
	for(int x=0;x<4;x++){
	  candidates[stage[y][x]]++;
	}

      }
      int res = 0;
      int count = 0;
      for(int card=1;card<=16;card++){
	if(candidates[card] >= 2){
	  res = card;
	  count++;
	}
      }
      
      if(count == 0){
	printf("Case #%d: Volunteer cheated!\n",test_idx);
      }
      else if(count == 1){
	printf("Case #%d: %d\n",test_idx,res);
      }
      else {
	//count > 1
	printf("Case #%d: Bad magician!\n",test_idx);
      }
    }
  }
}
