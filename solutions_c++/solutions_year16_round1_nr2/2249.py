#include<cstdio>
#include<queue>
#include<climits>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<ctype.h>
#include<set>
#include<vector>
#include<map>
#include<time.h>
#include<list>
#include<stack>
using namespace std;
#define mod 1000000007
#define mem(x) memset(x,0,sizeof(x))
#define pri printf
#define sca scanf

typedef long long LL;
const double PI=acos(-1.0);
const double  eps=1e-9;
int a[101][101];
int ans[101][101];
bool H[101],L[101];
int n;
bool  DFS(int x){
    bool f;
    int i,j;
//    pri("%d: \n",x);
//    for (i=0;i<n;i++){
//        for (j=0;j<n;j++) pri("%d ",ans[i][j]);
//        pri("\n");
//    }
    if (x==n*2-1){
        for (i=0;i<n;i++){
            if (!H[i]) {
                for (j=0;j<n;j++){
                    pri(" %d",ans[i][j]);
                }
            }
            if (!L[i]) {
                for (j=0;j<n;j++){
                    pri(" %d",ans[j][i]);
                }
            }
        }
        return 1;
    }
    for (i=0;i<n;i++){
        if (!H[i]){
            f=1;
            for (j=0;j<n;j++){
                if (ans[i][j]!=0&&ans[i][j]!=a[x][j]){f=0;break;}
            }
            if (f){
                int X[55];
                for (j=0;j<n;j++) {X[j]=ans[i][j];ans[i][j]=a[x][j];}
                H[i]=1;
                if (DFS(x+1)) return 1;
                H[i]=0;
                for (j=0;j<n;j++) ans[i][j]=X[j];
            }
        }
        if (!L[i]){
            f=1;
            for (j=0;j<n;j++){
                if (ans[j][i]!=0&&ans[j][i]!=a[x][j]){f=0;break;}
            }
            if (f){
                int xx[51];
                for (j=0;j<n;j++) {xx[j]=ans[j][i];ans[j][i]=a[x][j];}
                L[i]=1;
                if (DFS(x+1)) return 1;
                L[i]=0;
                for (j=0;j<n;j++) ans[j][i]=xx[j];
            }
        }
    }
    return 0;
}
int main(){
    int i,j,m;
    int T;
    freopen("B-small-attempt0 (1).in","r",stdin);
    freopen("D.out","w",stdout);
    sca("%d",&T);
    for (int cas=1;cas<=T;cas++){
        sca("%d",&n);
        for (i=0;i<2*n-1;i++){
            for (j=0;j<n;j++)
            {
                sca("%d",&m);
                a[i][j]=m;
            }
        }
        mem(H);
        mem(L);
        mem(ans);
        pri("Case #%d:",cas);
        DFS(0);
        pri("\n");
    }
    return 0;
}





















