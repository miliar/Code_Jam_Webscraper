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


int main(){
  int run, runs;
  scanf("%d\n",&runs);
  for(run=1;run<=runs;run++){
    long long k,c,s;
    scanf("%lld %lld %lld",&k,&c,&s);
    printf("Case #%d:",run);
    if (s*c<k){
      printf(" IMPOSSIBLE\n");
      continue;
    }
    for(int z=0;z<s;z++){
      long long curval=0;
      for(int q=0;q<c;q++){
        int _k = z*c+q;
        if (_k>=k) _k=0;
        curval=k*curval+_k;
      }
      if(z>0&&curval==0) break;
      printf(" %lld",curval+1);
    }
    printf("\n");
  }
}

