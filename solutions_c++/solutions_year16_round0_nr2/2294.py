#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

char t[1000];
int n;

int main()
{
  scanf("%d", &n);
  REP(ii,n){
    scanf("%s", t);
    char last = t[0];
    int i = 1;
    int w = 0;
    while (t[i] == '+' || t[i] == '-'){
       if (t[i] != last) w++;
       last = t[i];
       ++i;
    }
    if (last == '-') ++w;
    printf("Case #%d: %d\n", ii+1, w);
  }
    return 0;
}
