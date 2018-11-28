#ifndef INCLUDED
#include <bits/stdc++.h>
#define INCLUDED
#define F first
#define S second
#define MP make_pair
#define PB push_back

using namespace std;
typedef long long L;
typedef long double LD;
#endif
/*
 * Author: raghumdani
 * Date Created: 16/04/2016
*/

#define TESTCASE

const int N = 12345;
const int mod = 1000000007;

char s[N];

int GCJ_R1A_1S(int testNumber) {
  deque <char> dq;
  scanf("%s", s);

  int nn = strlen(s);
  for(int i  =0; i < nn; ++i) {
    if(dq.empty() || dq.front() <= s[i]) {
      dq.push_front(s[i]); 
    } else {
      dq.push_back(s[i]);
    }
  }
  printf("Case #%d: ", testNumber);
  while(!dq.empty()) {
    printf("%c", dq.front());
    dq.pop_front();
  }
  printf("\n");
}

void allClear() {
  
}

int main() {
  int t = 1;
  #ifdef TESTCASE
    scanf("%d", &t);
  #endif
  for(int _ = 1; _ <= t; ++_) {
    int ret = GCJ_R1A_1S( _ );
    allClear();
  }
  return(0);
}

