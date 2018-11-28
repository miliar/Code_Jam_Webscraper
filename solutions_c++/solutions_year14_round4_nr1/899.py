#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

int N,X;
map<int,int>A;

int run() {
  scanf("%d %d", &N, &X);
  A.clear();
  for(int i=0;i<N;++i){
    int a;
    scanf("%d", &a);
    A[a]++;
  }
  int res=0;
  while(A.size() > 0) {
    int x = A.rbegin()->first;
    if(!--A[x])A.erase(x);
    int r = X - x;
    map<int,int>::iterator it = A.upper_bound(r);
    if(it == A.begin()) {
      ++ res;
      continue;
    }
    ++ res;
    -- it;
    if(!--(it->second)) A.erase(it);
  }
  return res;
}

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  
  int test;
  scanf("%d", &test);
  int no=0;
  while(test--){
    printf("Case #%d: %d\n", ++ no, run());
  }
}


