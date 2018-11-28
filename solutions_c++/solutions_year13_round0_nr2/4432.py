#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <queue>
using namespace std;

#define FORN(i,n) for(int i=0; i<(n); i++)
#define EACH(p,c) for(typeof((c).begin()) p=(c).begin(); p!=(c).end(); p++)
typedef long long llint;

const int INF = (1<<29);
const llint LINF = (1LL<<61);
const double DINF = (1e100);

int main(int argc, char *argv[]) {
 //  freopen("B-small-attempt0.in", "r", stdin);
//   freopen("B-small-attempt1.in", "r", stdin);
//   freopen("B-small-attempt2.in", "r", stdin);
   freopen("B-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);

   int ncase; cin >> ncase;
   FORN(icase, ncase) {
       int N,M;
       int A[111][111];
       cin>>N>>M;
       FORN(i,N) FORN(j,M) cin >> A[i][j];

       set<int> canI;FORN(i,N)canI.insert(i);
       set<int> canJ; FORN(j,M) canJ.insert(j);

       bool ok=true;
       for(int cut=100;cut>0;cut--)
       {
           int can[111][111]={0};
           EACH(it,canI) FORN(j,M) can[*it][j]=1;
           EACH(jt,canJ) FORN(i,N) can[i][*jt]=1;

           FORN(i,N)FORN(j,M)if(A[i][j]==cut&&!can[i][j]) ok=false;
           if(!ok)break;
           FORN(i,N)FORN(j,M)if(A[i][j]==cut)
           {
               canI.erase(i);
               canJ.erase(j);
           }
       }
       cout<<"Case #"<<icase+1<<": "<<(ok?"YES":"NO")<<endl;

   }

   return 0;
}
