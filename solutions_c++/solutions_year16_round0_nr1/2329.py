#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define FOR(i,a,b) for (int i = a; i <= b; i++)
#define FORN(i,N) for (int i = 0; i < N; i++)
#define FORD(i,a,b) for (int i = a; i >= b; i--)


using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

bool check[10];

bool comp() {
  FORN(i,10)
    if(!check[i]) return false;
  return true;
}
char str[10000];
int main() {

  int T;
  scanf("%d",&T);

  FOR(c,1,T) {

      FORN(i,10) check[i] = false;
      int N;
      scanf("%d",&N);
      if(N == 0) printf("Case #%d: INSOMNIA\n",c);
      else
      for(int j=1;;j++) {
        int val = N*j;

        sprintf(str,"%d",val);
        
        FORN(i,strlen(str)) {
          check[str[i]-'0'] = true;
        }

        if(comp()) {
          printf("Case #%d: %d\n",c,val);
          break;
        }
      }
    } 
  
  
  return 0;
}
