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
  scanf("%d",&runs);
  for(run=1;run<=runs;run++){
    int n;
    scanf("%d",&n);
    vi counts(2501,0);
    for(int i=0;i<2*n-1;i++){
      for(int j=0;j<n;j++){
        int k;
        scanf("%d",&k);
        counts[k]++;
      }
    }
    printf("Case #%d:",run);
    for(int i=1;i<=2500;i++)
      if(counts[i]%2) printf(" %d",i);
    printf("\n");
  }
  return 0;
}

