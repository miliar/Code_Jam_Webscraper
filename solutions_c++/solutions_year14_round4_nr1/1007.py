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
const int MAX=111111; 
int n,x;
int a[MAX];
int mark[MAX];
int read(){
    scanf("%d %d",&n,&x);
    REP(i,n) scanf("%d",a+i);
    sort(a,a+n,greater<int>());
}
int process(){
    REP(i,n+5) mark[i]=0;
    int dem=0;
    REP(i,n){
        if (mark[i]) continue;
        FOR(j,i+1,n-1){
            if (!mark[j] && a[i]+a[j]<=x) {
                mark[i]=1;
                mark[j]=1;
                dem++;
                break;
            }
        }
        if(!mark[i]) {
            mark[i]=1;
            dem++;
        }
    }
    printf("%d", dem);
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
