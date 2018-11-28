//Program: c
//Author: gary
//Date: 13/04/2013
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <limits>
#include <string>
#include <iostream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define CNT(c,x) ((c).find(x) != (c).end())
#define FOR(i, a, n) for(int i=(a);i<=(n);i++)
#define REP(i, n) for(int i=0;i<(n);i++)
#define REP1(i, n) for(int i=0;i<=(n);i++)
#define DBG(VAR) cerr<<#VAR<<" = "<<(VAR)<<endl;
#define CLR(x, v) memset(x, v, sizeof(x))
#define SZ(x) ( (int) (x).size() )
#define MP(x, y) make_pair( (x), (y) )
#define MP3(x, y, z) MP( (x), MP( (y), (z) ) )
#define MP4(x1, y1, x2, y2) MP( MP(x1, y1), MP(x2, y2) )
#define foreach(it, C) for(typeof((C).begin())it=(C).begin();it!=(C).end();++it)
#define pb push_back
typedef long long LL;
typedef pair<int, int> PII;
template<class T> bool checkMin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool checkMax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
//int dx[]={-1,0,1,0},  dy[]={0,1,0,-1};
//int dx[]={-1,-1,0,1,1,1,0,-1},dy[]={0,1,1,1,0,-1,-1,-1};
const int INF = 1e9;
const int MN = 100;
int s[MN+1];

int lim;
LL N;
int toarr(LL a){ // returns length, and saved reversed
  int p = 0;
  while(a > 0)
    s[p++] = a % 10, a /= 10;
  return p;
}
LL mirror(LL a, int offset){
  int i = offset, n = toarr(a);
  while(i < n)
    a = (a * 10) + s[i++];
  return a;
}
LL sq(LL a){return a * a;}

bool isPalindrome(LL x){
  //  printf("in(%lld)\n", x);
  if(x > N || x == 0)
    return false;
  // printf("Testing: %lld N=%lld\n", x, N);
  int i = 0, j = toarr(x) - 1;
  while(i < j){
    if(s[i] != s[j])
      return false;
    i++, j--;
  }
  return true;
}


LL rec(LL have, int len){
  if(len == lim){
    return isPalindrome( sq(mirror(have, 0)) ) + isPalindrome( sq(mirror(have, 1)));
  }
  have *= 10;
  LL ans = 0;
  for(int i = 0; i < 10; i++)
    ans += rec(have++, len + 1);
  return ans;
}

LL solve(LL n){
  LL ans = 0;
  lim = 1;
  N = n;
  while(lim <= 1){
    ans += rec(0, 0);
    lim++;
  }
  return ans;
}

int main(){
  int T;  scanf("%d", &T);
  FOR(t, 1, T){
    LL L, R; scanf("%lld %lld", &L, &R);
    printf("Case #%d: %lld\n", t, solve(R)-solve(L-1));
  }
}
