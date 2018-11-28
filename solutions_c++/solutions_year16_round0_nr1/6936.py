#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include <ctime>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<iomanip>
#include<cmath>
#define mst(ss,b) memset((ss),(b),sizeof(ss))
#define maxn 0x3f3f3f3f
#define MAX 1000100
///#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
typedef unsigned long long ull;
#define INF (1ll<<60)-1
using namespace std;
int n;
int vis[22];
bool pd(ll t){
    while(t){
        int x=t%10;
        t/=10;
        vis[x]=1;
    }
    for(int i=0;i<=9;i++) {
        if(!vis[i]) return true;
    }
    return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d",&n);
        printf("Case #%d: ",cas);
        if(n==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        mst(vis,0);
        ll t=n;
        while(pd(t)) t=t+n;
        printf("%I64d\n",t);
    }
    return 0;
}
