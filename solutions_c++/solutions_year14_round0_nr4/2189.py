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
      int N;
      scanf("%d",&N);

      vector<double> naomi;
      vector<double> ken;
      for(int i=0;i<N;i++){
	double w;
	scanf("%lf",&w);
	naomi.push_back(w);
      }
      for(int i=0;i<N;i++){
	double w;
	scanf("%lf",&w);
	ken.push_back(w);
      }

      sort(ken.begin(),ken.end());
      sort(naomi.begin(),naomi.end());
      
      int war = 0;
      bool w_used[1001];
      memset(w_used,false,sizeof(w_used));
      for(int i=0;i<N;i++){
	bool isok = false;
	for(int j=0;j<N;j++){
	  if(naomi[i] < ken[j]
	     && !w_used[j]){
	    w_used[j] = true;
	    isok = true;
	    break;
	  }
	}

	if(!isok){
	  war++;
	  for(int j=0;j<N;j++){
	    if(!w_used[j]){
	      w_used[j] = true;
	      break;
	    }
	  }
	}
      }

      sort(naomi.begin(),naomi.end(),greater<double>());
      int dwar = 0;
      bool dw_used[1001];
      memset(dw_used,false,sizeof(dw_used));

      for(int i=0;i<N;i++){
	bool isok = false;
	for(int j=N-1;j>=0;j--){
	  if(naomi[i] > ken[j]
	     && !dw_used[j]){
	    dw_used[j] = true;
	    isok = true;
	    dwar++;
	    break;
	  }
	}
      }
      printf("Case #%d: %d %d\n",test_idx,dwar,war);
    }
  }
}
