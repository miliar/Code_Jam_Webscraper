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
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

struct elem {
  int v, pos;
};

bool operator<(const elem &a, const elem &b) {
  return a.v<b.v;
}

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    scanf("%d",&k);
    vi s(k);
    for(i=0;i<k;i++) scanf("%d", &s[i]); 

    int best = 0;
    vector<elem> vec;
    for(i=0;i<sz(s);i++) {
      elem a; a.v=s[i]; a.pos=i; vec.pb(a);
    }
    sort(vec.begin(), vec.end());
    for(i=0;i<k;i++) {
      int L=0,R=0;
      for(j=i+1;j<k;j++) {
        if(vec[j].pos<vec[i].pos) L++; else R++;
      }

      best+=min(L,R);
    }

    printf("Case #%d: %d\n", _case, best);
  }

  return 0;
}
