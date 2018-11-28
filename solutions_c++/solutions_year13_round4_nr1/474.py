#include <algorithm>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=((int)(a))-1; i>=(b); --i)

#define pb push_back
#define mp make_pair
#define st first
#define nd second

lint modulo = 1000002013LL;

void rob(){
    int n,m;
    scanf("%d%d",&n,&m);
    vector<PII> poczatki;
    vector<PII> konce;
    lint res1 = 0;
    int a,b,c;
    FOR(i,0,m){
        scanf("%d%d%d",&a,&b,&c);
        poczatki.pb(mp(a,c));
        konce.pb(mp(b,c));
        res1 = (res1+ c*1LL*(b-a)*1LL*(b-a-1)/2)%modulo;
    }
    lint res2=0LL;
    lint krotkie = 1000*1000*1001;
    PII dla;
    int ile = 2*m;
    while(ile>0){
      FOR(i,0,poczatki.size()){
          FOR(j,0,konce.size()){
              if(poczatki[i].nd>0 && konce[j].nd > 0){
                if( (-poczatki[i].st+konce[j].st) >=0 && (-poczatki[i].st+konce[j].st)<krotkie){
                    krotkie = konce[j].st-poczatki[i].st;
                    dla = mp(i,j);
                }
              }
          }
      }
      //cout<<"DUPA"<<endl;
      int cos = min(poczatki[dla.st].nd,konce[dla.nd].nd);
      res2+= (cos*((konce[dla.nd].st-poczatki[dla.st].st)*1LL*(konce[dla.nd].st-poczatki[dla.st].st-1)/2)%modulo)%modulo;
      poczatki[dla.st].nd-=cos;
      konce[dla.nd].nd-=cos;
      if(poczatki[dla.st].nd==0) ile--;
      if(konce[dla.nd].nd==0) ile--;
      krotkie = 1000*1000*1001;
    }
    lint res;
    if(res2-res1 > 0) res=(res2-res1)%modulo;
    else res = (res2-res1+modulo)%modulo;
    printf("%lld\n", res);



    
}

int main(){
    int testy; scanf("%d",&testy);
    FOR(ntest,1,testy+1){
        printf("Case #%d: ",ntest);
        rob();
    }
    return 0;
}
