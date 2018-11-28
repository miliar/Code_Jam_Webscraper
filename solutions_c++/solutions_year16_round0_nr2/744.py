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
  int run,runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++){
    char buf[10000];
    scanf("%s",buf);
    string s=buf;
    s+="+";
    int tel=0;
    for(int i=0;i<sz(s)-1;i++)
      if(s[i]!=s[i+1])
        tel++;
    printf("Case #%d: %d\n",run,tel);
  }
}

