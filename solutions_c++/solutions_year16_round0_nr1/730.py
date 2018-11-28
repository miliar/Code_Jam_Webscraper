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

long long solve(long long in){
  if (in == 0) return -1;
  int used = 0;
  for(int i=1;i<=1000000;i++){
    long long v = i*in;
    while(v){
      used|=1<<(v%10);
      v/=10;
    }
    if(used==(1<<10)-1)
      return i*in;
  }
  return -1;
}

int main(){
  int run,runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++){
    long long n; scanf("%lld",&n);
    long long res = solve(n);
    printf("Case #%d: ",run);
    if(res==-1)
      printf("INSOMNIA\n");
    else
      printf("%lld\n",res);
  }
}

