#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define For(Q,W) for(int Q=0;Q<W;Q++)
#define Forl(Q,W) for(long long Q=0;Q<W;Q++)
#define LLD long long
#define pfnl printf("\n")

//#define debug
#ifdef debug
#define db(EE) cout<<EE<<" "
#define dbn(EE) cout<<EE<<" "<<endl;
#else
#define db(EE) 
#define dbn(EE) 
#endif


void solve(int test){
    int n,m;
    scanf("%d %d ",&n,&m); 
    int pole[n][m];
    For(i,n)
    For(j,m) scanf(" %d ",&pole[i][j]);
    
    int riadm[n];
    int stlpm[m];
    fill(riadm,riadm+n,-1);
    fill(stlpm,stlpm+m,-1);
    
    For(i,n) For(j,m){
        riadm[i]=max(riadm[i],pole[i][j]);
        stlpm[j]=max(stlpm[j],pole[i][j]);   
    }
    
    bool ok=true;
    For(i,n) For(j,m){
        if(pole[i][j]!=riadm[i] && pole[i][j]!=stlpm[j]) ok=false;   
    }
    
    printf("Case #%d: ",test);
    if(ok) printf("YES\n");
    else printf("NO\n");

}


int main(){

int t;
scanf("%d ",&t);

For(i,t){
solve(i+1);
}

return 0;
}
