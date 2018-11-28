#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 13
#define MAXS (1<<13)

char lets[] = {'P','R','S'};
string solve(int N, int top) {
  if (N==0) return string(1,lets[top]);
  int a = (top)%3;
  int b = (top+1)%3;
  string X = solve(N-1,a);
  string Y = solve(N-1,b);
  if (X<Y) return X+Y;
  return Y+X;
}

bool is_valid(string T, int P, int R, int S) {
  int N = T.size();
  FOR(i,N) {
    if (T[i] == 'P') P--;
    else if (T[i] == 'R') R--;
    else if (T[i] == 'S') S--;
    else assert(false);
  }
  return P>=0 && R>=0 && S>=0;
}

string solve(int N, int P, int R, int S) {
  string A = solve(N,0);
  string B = solve(N,1);
  string C = solve(N,2);

  if (A>B) swap(A,B);
  if (A>C) swap(A,C);
  if (B>C) swap(B,C);
  assert(A<=B && B<=C);

  if (is_valid(A,P,R,S)) return A;
  if (is_valid(B,P,R,S)) return B;
  if (is_valid(C,P,R,S)) return C;
  return "IMPOSSIBLE";
}

int main() {
  int TEST,N,P,R,S;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    scanf("%d%d%d%d",&N,&R,&P,&S);
    string ans = solve(N,P,R,S);
    printf("Case #%d: %s\n",test+1,ans.c_str());
  }
}















