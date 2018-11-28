#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>
#include <iostream>
#include <ctime>

using namespace std;
#define TASKNAME "code"
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);i++)
const int MAX=1111; 
int n,x;
int a[MAX];
int l[MAX],r[MAX];
int f[MAX][MAX];
vector< int* >rr;
int read(){
    rr.clear();
    scanf("%d",&n);
    REP(i,n) {
        scanf("%d",a+i);
        rr.push_back(&a[i]);
    }
    
}
int comp(int* l, int* r){
    return *l < *r;
}
int process(){
    sort(rr.begin(),rr.end(),comp);
    REP(i,rr.size()) *rr[i]=i+1;
    REP(i,n+1) l[i]=0,r[i]=0;
    FOR(i,0,n) FOR(j,0,n) f[i][j]=0;
    REP(i,n){
        REP(j,i) if (a[j]>a[i]) l[a[i]]++;
        FOR(j,i+1,n-1) if (a[j]>a[i]) r[a[i]]++;
    }
    // FOR(i,1,n) printf("%d ", r[i]);
    FOR(i,1,n) {
        f[0][i]=f[0][i-1]+r[i];
        f[i][0]=f[i-1][0]+l[i];
    }
    FOR(i,1,n){
        FOR(j,1,n){
            if (i+j>n) continue;
            if (i+j==0) continue;
            f[i][j]=f[i-1][j]+l[i+j];
            f[i][j]=min(f[i][j],f[i][j-1]+r[i+j]);
        }
    }
    // FOR(i,0,n){
    //     FOR(j,0,n) printf("%d ", f[i][j]);
    //     printf("\n");
    // }
    int ans=1000000000;
    FOR(i,0,n) ans=min(ans,f[i][n-i]);
    printf("%d", ans);
}
int main(){
    #ifndef ONLINE_JUDGE
    freopen(TASKNAME".inp","r",stdin);
    freopen(TASKNAME".out","w",stdout);
    #endif // ONLINE_JUDGE
    int sotest;
    scanf("%d",&sotest);
    // sotest=1;
    for (int test=1;test<=sotest;test++){
        printf("Case #%d: ",test);
        read();
        process();
        printf("\n");
    }

    return 0;
}
