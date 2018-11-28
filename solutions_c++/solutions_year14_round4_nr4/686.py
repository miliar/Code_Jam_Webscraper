#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

int triesz(vs w) {
  if(sz(w)==0) return 0;
  vi leeg(26,-1);
  vvi trie(1, leeg);
  for(int i=0;i<sz(w);i++) {
    int k=0;
    for(int j=0;j<sz(w[i]);j++) {
      int L=w[i][j]-'A';
      if(trie[k][L]!=-1) {
        k=trie[k][L];
      } else {
        trie[k][L] = sz(trie);
        k=sz(trie);
        trie.pb(leeg);
      }
    }
  }
  //printf("sz(w) %d -> sz(trie) %d\n", sz(w),sz(trie));
  return sz(trie);
}

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    int m,n; scanf("%d %d",&m, &n);
    vs w;
    for(i=0;i<m;i++) {scanf("%s",buf); w.pb(buf); }
    int worst=-1, aant=0;
    for(int s=0;s<(1<<(2*m));s++) {  //allocation
      bool isok=true;
      int _s=s;
      for(i=0;i<m;i++) {  
        int q=_s%4; _s/=4;
        if(q>=n) {isok=false; break;}
      }
      if(!isok) continue;

      int nodes=0;
      for(int serv=0;serv<n;serv++) {
        vs _w;
        _s=s;
        for(i=0;i<m;i++) {  
          int q=_s%4; _s/=4;
          if(q==serv) _w.pb(w[i]);
        } 
        nodes+=triesz(_w);
      }

      if(nodes>worst) {
        worst=nodes; aant=1;
      } else if(worst==nodes) {
        aant++;
      }
      //printf("nodes = %d, worst=%d, aant=%d\n", nodes, worst, aant);
    }

    printf("Case #%d: %d %d\n", _case, worst, aant); 
  }


  return 0;
}
