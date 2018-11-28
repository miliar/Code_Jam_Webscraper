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

//#define DBG(a,...)
#define DBG printf

typedef unsigned long long u64;

using namespace std;

u64 P,Q;
int mingen = 999999;

u64 gcd(u64 a, u64 b)
{
  u64 c = a % b;
  while(c != 0)
  {
    a = b;
    b = c;
    c = a % b;
  }
  return b;
}

bool breed(int gen, u64 A, u64 B, u64 C, u64 D, int sinceFull)
{
  if (gen == 10) {
    return false;
  }
  if (sinceFull >= mingen) {
    return false;
  }

  u64 pn = (A*D + C*B);
  u64 qn = 2*B*D;

  u64 gc = gcd(pn,qn);
  pn = pn / gc;
  qn = qn / gc;

  //  DBG("test P/Q %lld/%lld == pn/qn %lld/%lld\n", P, Q, pn, qn);

  if (pn == P && qn == Q) {
    //    DBG("FOUND! gen %d\n", gen);
    // yes!
    if (sinceFull < mingen) {
      //  DBG("HIGH!\n");
      mingen = sinceFull;
    }
    //correct = gen;
    return true;
  }

  breed(gen + 1, pn, qn, 0, 1, sinceFull + 1);
  breed(gen + 1, pn, qn, 1, 1, 1);


  return true;
}

int main()
{
  int tn;
  int v = scanf("%d",&tn);
  (void)v;

  bool imp;

  int ti = 1;
  while(tn) {

    imp = true;
    int gen = 0;
    mingen = 999999;

    v = scanf("%lld/%lld",&P,&Q);

    // 1 <= p <= Q <= 10*12   P/Q can be  10/20 gcd?


    u64 g = gcd(P,Q);
    //DBG("gcd=%lld\n", g);
    P = P/g;
    Q = Q/g;

    //DBG("%lld %lld\n",P,Q);

    if ((P == 1 && Q == 1) ||
        (P == 0) ||
        ((P == 1) && (Q == 2))) {
      gen = 1;  // if not elf or full elf of half
      mingen = 1;
      imp = false;
    }
    else {
      gen = 0;
      breed(gen+1, 0,1,1,1, 1); // try 0 and 1
      
      if (mingen < 1000) {
        imp = false;
      }
    }


    if (imp) {
      printf("Case #%d: impossible\n", ti);
    }
    else {
      printf("Case #%d: %d\n", ti, mingen);
    }

    ti++;
    tn--;
  }

  return 0;
}
