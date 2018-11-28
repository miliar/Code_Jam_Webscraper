#include <iostream>
#include <sstream>
#include <cstring>
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
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())

struct attack{
  int w,e,s;
};


int main()
{
  int i,j,k,l; char buf[1000];
  int keeses, kees;
  scanf("%d",&keeses);
  for(kees=1;kees<=keeses;kees++) {
    map<int, vector<attack> > A;
    int N; scanf("%d",&N);
    for(k=0;k<N;k++) {
      int d,n,w,e,s,delta_d,delta_p,delta_s;
      scanf("%d %d %d %d %d %d %d %d",&d,&n,&w,&e,&s,&delta_d,&delta_p,&delta_s);
      for(i=0;i<n;i++) {
        attack a;
        a.w=w+i*delta_p;
        a.e=e+i*delta_p;
        a.s=s+i*delta_s;
        A[d+i*delta_d].pb(a);
      }
    }

    map<int, int> W;
    int ans=0;

    for(map<int,vector<attack> >::iterator I=A.begin();I!=A.end();I++) {
      for(int m=0;m<sz((*I).second);m++) {
        attack a=(*I).second[m];
//printf("[%d,%d] met strength %d\n",a.w, a.e,a.s);
        for(i=a.w;i<a.e;i++) {
          if(a.s>W[i]) { ans++; break; }
        }      
      }
      for(int m=0;m<sz((*I).second);m++) {
        attack a=(*I).second[m];
        for(i=a.w;i<a.e;i++) {
          int nuw=W[i];
          W[i]=max(nuw,a.s);
        }      
      }
    }

    printf("Case #%d: %d\n",kees,ans);
  }


  return 0;
}
