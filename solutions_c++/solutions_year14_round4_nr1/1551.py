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
typedef long double ld;
using namespace std;

int T,N,X,a;
set<pair<int,int> > S;

int main(){
  scanf("%d ", &T);
  For(t,T){
    scanf("%d %d", &N, &X);
    For(i,N){ scanf("%d", &a); S.insert(mp(a,i)); }
    int vys = 0;
    set<pair<int,int> >::iterator it;
    while(!S.empty()){
      vys++;
      it = S.end(); --it;
      int sp = X - (*it).first;
      S.erase(it);
      it = S.upper_bound(mp(sp,N));
      if(it==S.begin()) continue;
      --it;
      if((*it).first <= sp) S.erase(it);
    }
    
    printf("Case #%d: %d\n",t+1,vys);
  }
  return 0;
}