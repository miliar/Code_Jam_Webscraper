// last update : 2013-04-13 16:20:57 nav

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;
typedef long long ll;

#define ALL(a)  (a).begin(),(a).end()

const int INF = 1 << 29;
const double EPS = 1e-7;

int main(int argc, char **argv){
  int T;
  FILE *fp;
  fp = fopen("B-large.in", "r");
  fscanf(fp, "%d", &T);
  for(int i = 0; i < T; i++){
    int N, M;
    fscanf(fp, "%d %d", &N, &M);
    int lawn[100][100];
    
    set<int> height;
    for(int y = 0; y < N; y++)
      for(int x = 0; x < M; x++){
	fscanf(fp, "%d", &lawn[y][x]);
	height.insert(lawn[y][x]);
      }
  
    int ymax[100] = {0};
    int xmax[100] = {0};
    for(int y = 0; y < N; y++){
      for(int x = 0; x < M; x++){    
	xmax[y] = max(xmax[y], lawn[y][x]);
      }
    }
    for(int x = 0; x < M; x++){
      for(int y = 0; y < N; y++){    
	ymax[x] = max(ymax[x], lawn[y][x]);
      }
    }

    bool isok = true;
    for(set<int>::iterator it = height.begin(); 
	it != height.end(); it++){
      if(++it == height.end() && height.size() > 1) break;
      else it--;

      bool isthis = true;
      for(int y = 0; y < N; y++){
	for(int x = 0; x < M; x++){
	  if(lawn[y][x] == *it){
	    bool xline = true;
	    bool yline = true;
	    
	    if(ymax[x] > *it){
	      yline = false;
	    }
	    
	    if(xmax[y] > *it){
	      xline = false;
	    }
	    
	    if(!xline && !yline)
	      isthis &= false;
	  }
	}
      }
      isok &= isthis;
      if(!isthis) break;
    }
    if(isok)
      cout << "Case #" << i + 1 << ": YES" << endl;
    else
      cout << "Case #" << i + 1 << ": NO" << endl;
  }
}
