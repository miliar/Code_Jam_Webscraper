#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <bitset>

#include <math.h>

#define DBG(a,...)
//#define DBG printf

typedef unsigned long long u64;

using namespace std;

char cars[101][101];
int siz[101];
int occur[256];

int main()
{
  int tn;
  int v = scanf("%d",&tn);
  (void)v;

  int ti = 1;
  while(tn) {

    int N;

    v = scanf("%d",&N);

    DBG("%d\n",N);

    u64 npos = 0;

    memset(cars,0,101*101);
    memset(siz,0,101*sizeof(int));


    int n;
    for (n = 0; n < N; n++) {
      int res = scanf("%s", cars[n]);
      DBG("A=%s\n", cars[n]);
      (void)res;
      siz[n] = strlen(cars[n]);
    }


    
    // try all perm


    int pp[N];
    int i;
    for (i = 0; i < N; i++) {
      pp[i] = i;
    }
    do {
      for (i = 0; i < N; i++) {
        DBG(" %d,", pp[i]);
      }
      DBG("\n");



      memset(occur,0,256*sizeof(int));

      bool possib = true;
      char lastc = '?';

      // all cars
      for (i = 0; i < N; i++) {
        int si;    
        int mx = siz[ pp[i] ];
        // all string
        for (si = 0; si < mx; si++) {
          char cc = cars[ pp[i] ][ si ];
          // new char
          if (cc != lastc) {
            lastc = cc;
            if (occur[ (int)cc ] == 1) {
              // occured: false;
              possib = false;
              goto not_poss;
            }
            else {
              occur[ (int)cc ] = 1;
            }
          }
        }
      }
      
    not_poss:
      if (possib) {
        npos++;
      }


    } while (next_permutation(pp,pp+N));
    


    

    printf("Case #%d: %lld\n", ti, (npos % 1000000007ULL));

    ti++;
    tn--;
  }

  return 0;
}
