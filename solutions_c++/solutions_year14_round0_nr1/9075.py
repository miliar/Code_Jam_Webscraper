#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define all(a) (a).begin(),(a).end()

int T;

int ans0, ans1;
int f[10][10];
int s[10][10];

void input() {
  scanf("%d", &ans0);
  --ans0;
  rep(i,4) {
    rep(j,4) {
      scanf("%d", f[i] + j);
    }
  }
  scanf("%d", &ans1);
  --ans1;
  rep(i,4) {
    rep(j,4) {
      scanf("%d", s[i] + j);
    }
  }
}


int flag[20];
void solve(int caseNum) {
  memset(flag, 0, sizeof flag);
  rep(i,4) {
    flag[ f[ans0][i] ] += 1;
    flag[ s[ans1][i] ] += 1;
  }

  int val = count(flag, flag + 20, 2);
  if(val == 0) {
    printf("Case #%d: Volunteer cheated!\n", caseNum);
    return;
  }
  else if (val == 1) {
    printf("Case #%d: %ld\n", caseNum, find(flag, flag + 20, 2) - flag);
    return;
  }
  printf("Case #%d: Bad magician!\n", caseNum);
}

int main() {
  scanf("%d", &T);
  rep(z,T) {
    input();
    solve(z+1);
  }
  return 0;
}
