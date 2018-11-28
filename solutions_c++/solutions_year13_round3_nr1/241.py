#include <iostream>
#include <sstream>
#include <cstring>
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
#define sz(v) (int)(v.size())

char buf[1000010];

int main()
{
  int i,j,k;
  int keeses; scanf("%d",&keeses);
  for(int kees=1;kees<=keeses;kees++) {
    long long ant=0,l,m,r,n,s;

    scanf("%s %lld", buf, &n);
    int lastn=-1; int now=0;
    for(i=0;buf[i];i++) {
      if(buf[i]=='a'||buf[i]=='e'||buf[i]=='i'||buf[i]=='o'||buf[i]=='u') {
        now=0;
      } else {
        now++;
        if(now>=n) lastn=i;
      }
      if(lastn!=-1) {
        ant+=lastn-n+2;
      }

    } 

    printf("Case #%d: %lld\n", kees, ant);
  }

  return 0;
}
