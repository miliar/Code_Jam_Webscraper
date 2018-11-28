#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

typedef pair<int,int> pairii;
typedef long long llong;

#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

const int MAXN=2005;
char DIGIT[20][20]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char s[MAXN];
int cnt[26],n;
int res[10];

void solve() {
  cin>>s;
  memset(cnt,0,sizeof cnt);
  memset(res,0,sizeof res);
  n=(int)strlen(s);
  FORZ(i,n) cnt[s[i]-'A']++;
  res[0]=cnt['Z'-'A'];
  res[2]=cnt['W'-'A'];
  res[4]=cnt['U'-'A'];
  res[6]=cnt['X'-'A'];
  res[8]=cnt['G'-'A'];
  for(int i=0;i<10;i+=2) {
    FORZ(j,strlen(DIGIT[i])) {
      cnt[DIGIT[i][j]-'A']-=res[i];
    }
  }
  res[1]=cnt['O'-'A'];
  res[3]=cnt['R'-'A'];
  res[5]=cnt['F'-'A'];
  res[7]=cnt['S'-'A'];
  for (int i=1; i<=7; i+=2) {
    FORZ(j,strlen(DIGIT[i])) {
      cnt[DIGIT[i][j]-'A']-=res[i];
    }
  }
  res[9]=cnt['I'-'A'];
  FORZ(i,10) {
    FORZ(j,res[i]) {
      cout<<i;
    }
  }
  cout<<"\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
