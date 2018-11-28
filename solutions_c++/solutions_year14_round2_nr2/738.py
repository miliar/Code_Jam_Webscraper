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
#include <stack>
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

int T,A,B,K;

int main(){
  scanf(" %d", &T);
  For(t,T){
    scanf(" %d %d %d", &A, &B, &K);
    int poc = 0;
    For(i,A) For(j,B) if( (i & j) < K) poc++;
    printf("Case #%d: %d\n",t+1, poc);
  }
  return 0;
}