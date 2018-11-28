#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

int A, N;
vector<int> o;

int solve(int i,int n,int a) {
  if (a==1) return n;
  if (i==n) return 0;
  if(a>o[i]){
    a+=o[i];
    return solve(i+1,n,a);
  }else{
    a+=(a-1);
    return 1+solve(i,n,a);
  }
}

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    cin >> A >> N;
    o.resize(N);
    rep(i,N) cin>>o[i]; sort(all(o));

    int ans = N;
    if (A==1) {
      ;
    } else {
      for (int n=N; n>0; --n) {
        int ax = solve(0,n,A) + (N-n);
        if (ax < ans) ans = ax;
      }
    }
    printf("Case #%d: %d\n", 1+_t, ans);
  }
}
