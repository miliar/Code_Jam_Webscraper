#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define Fore(i,C) for(__typeof((C).begin()) i =(C).begin(); i != (C).end(); ++i)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define Fors(i,s) for(int i=0; s[i]; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;
using namespace std;

int T;
long double C,F,X;
long double cook, mini, tim,prod;

int main(){
  scanf(" %d ",&T);
  For(t,T){
    scanf(" %Lf %Lf %Lf ",&C, &F, &X);
    prod = 2; mini = X/2; tim=0;
    while(tim < mini){
      tim += C/prod;
      prod += F;
      mini = min( mini, tim + X/prod);
    }
    printf("Case #%d: %0.7Lf\n",t+1,mini);
  }
  return 0;
}