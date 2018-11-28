#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXS = 1005;
char audience[MAXS];

int main(void) {
  int T;
  scanf("%d", &T);
  for(int kase = 1; kase <= T; kase++) {
    int res = 0, clap = 0, S;
    scanf("%d", &S);
    scanf("%s", audience);
    for(int req = 0; req <= S; ++req) {
      if(audience[req] > '0' && req > clap) {
        res += req - clap;
        clap = req;
      }
      clap += audience[req] - '0';
    }
    printf("Case #%d: %d\n", kase, res);
  }
  return 0;
}
