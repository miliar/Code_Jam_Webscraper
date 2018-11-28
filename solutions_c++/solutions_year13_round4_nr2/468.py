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

lint potegi[60];

lint najgorsze(lint x,int n){
     if(x==0) return 0;
     else{
         return najgorsze( (x+1)/2-1,n-1)+potegi[n-1];
     }
}

lint najlepsze(lint x,int n){
    if(x==(potegi[n]-1)) return x;
    else{
        return najlepsze((x+1)/2,n-1 );
    }
}

void rob(){
    int n; scanf("%d",&n);
    lint p; scanf("%lld",&p);
    p--;
    lint lewy=0LL,prawy = potegi[n]-1;
    while(prawy-lewy>1LL){
        //cout<<lewy<<" LP "<<prawy<<endl;
        lint sr = (lewy+prawy)/2;
        //cout<<sr<<" sr najg "<<najgorsze(sr,n)<<endl;
        if(najgorsze(sr,n)>p){
              prawy = sr;
        }
        else lewy = sr;
    }
    lint res1 =0LL;
    //cout<<najgorsze(prawy,n)<<endl;
    if( najgorsze(prawy,n)>p) res1 = lewy;
    else res1 = prawy;
    
    lewy = 0LL; prawy = potegi[n]-1;
    while(prawy-lewy>1LL){
        lint sr = (lewy+prawy)/2;
        if(najlepsze(sr,n)<=p) lewy = sr;
        else prawy = sr;
    }
    lint res2=0LL;
    if( najlepsze(prawy,n)<=p) res2 = prawy;
    else res2 = lewy;
    printf("%lld %lld\n",res1,res2);
}

int main(){
    potegi[0]=1LL;
    FOR(i,1,52) potegi[i]=potegi[i-1]*2LL;
    int testy; scanf("%d",&testy);
    FOR(ntest,1,testy+1){
        printf("Case #%d: ",ntest);
        rob();
    }
    return 0;
}
