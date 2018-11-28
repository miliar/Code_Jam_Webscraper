#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <complex>
#include <fstream>
#include <iomanip> //setprecision會用到的函式庫
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define debug puts("yejinru")
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define foreach(i,vec) for(int i=0;i<(int)vec.size();i++)
#define pb push_back
#define RD(n) scanf("%d",&n)
#define RD2(x,y) scanf("%d%d",&x,&y)
#define RD3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define RD4(x,y,z,w) scanf("%d%d%d%d",&x,&y,&z,&w)
#define All(vec) vec.begin(),vec.end()
#define MP make_pair
#define PII pair<int,int>
#define PQ priority_queue
#define cmax(x,y) x = max(x,y)
#define cmin(x,y) x = min(x,y)
#define Clear(x) memset(x,0,sizeof(x))
#define lson rt<<1
#define rson rt<<1|1
#define SZ(x) x.size()

/*

#pragma comment(linker, "/STACK:1024000000,1024000000")

int ssize = 256 << 20; // 256MB
char *ppp = (char*)malloc(ssize) + ssize;
__asm__("movl %0, %%esp\n" :: "r"(ppp) );

*/

char IN;
bool NEG;
inline void Int(int &x){
    NEG = 0;
    while(!isdigit(IN=getchar()))
        if(IN=='-')NEG = 1;
    x = IN-'0';
    while(isdigit(IN=getchar()))
        x = x*10+IN-'0';
    if(NEG)x = -x;
}
inline void LL(ll &x){
    NEG = 0;
    while(!isdigit(IN=getchar()))
        if(IN=='-')NEG = 1;
    x = IN-'0';
    while(isdigit(IN=getchar()))
        x = x*10+IN-'0';
    if(NEG)x = -x;
}

/******** program ********************/



int main(){

#ifndef ONLINE_JUDGE
    freopen("sum.in","r",stdin);
    freopen("sum.out","w",stdout);
#endif

    int ncase,cnt = 0;
    RD(ncase);
    while(ncase--){
        printf("Case #%d: ",++cnt);
        long double c,f,x;
        cin>>c>>f>>x;
        long double ans = x/2;
        long double v = 2;
        long double tot = 0;
        while(1){
            tot += c/v;
            v += f;
            double tmp = x/v+tot;
            if(tmp<ans)
                ans = tmp;
            else
                break;
        }
        cout<<fixed<<setprecision(7)<<ans<<endl;
    }

    return 0;
}
