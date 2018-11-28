#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

vi bff;
int best =0;
int state[10000]; //kid indices
int n;

void dfs(int used, int depth){
  
  bool isvalid=true;
  for(int i=0;i<depth;i++) {
    if(bff[state[i]]!=state[(i+1)%depth]&&bff[state[i]]!=state[(i+depth-1)%depth])
    { isvalid=false; break;}
  }
  if(isvalid) best=max(best, depth);
  
  if(depth<n){
    for(int i=0;i<n;i++) if(!(used & (1<<i))) {
      state[depth]=i;
      dfs(used|(1<<i), depth+1);
    }
  }
}


int main(){
  int run, runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++){
    scanf("%d",&n);
    bff = vi(n, 0);
    for(int i=0;i<n;i++) {scanf("%d",&bff[i]); bff[i]--;}
    best=0;
    dfs(0, 0);
    printf("Case #%d: %d\n",run,best);
  }
  return 0;
}

