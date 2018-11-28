//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <string>
#include <stack>
#include <sstream>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a));
#define INF 0x3f3f3f3f
#define lldINF 0x3f3f3f3f3f3f3f3fll
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define MP make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using std::bitset;
using namespace std;

#define maxn 103

int a[maxn][maxn],flag[maxn][maxn];
int n,m,ans;

int judge(){
    int i,j,tem,mark;
    while (1){
        mark=0;
        for (i=1; i<=n; i++){
            int mm=-1;
            for (j=1; j<=m; j++)
                if (flag[i][j]==0 && a[i][j]>mm) mm=a[i][j];

            for (j=1; j<=m; j++)
                if (flag[i][j]==0 && a[i][j]<mm) break;
            if (j>m){
                for (j=1; j<=m; j++){
                    if (mm!=-1 && flag[i][j]!=0 && flag[i][j]>mm) return 0;
                    if (flag[i][j]==0){flag[i][j]=mm; mark=1;}
                }
            }
        }
        for (j=1; j<=m; j++){
            int mm=-1;
            for (i=1; i<=n; i++)
                if (flag[i][j]==0 && a[i][j]>mm) mm=a[i][j];
            for (i=1; i<=n; i++)
                if (flag[i][j]==0 && a[i][j]<mm) break;
            if (i>n){
                for (i=1; i<=n; i++){
                    if (mm!=-1 && flag[i][j]!=0 && flag[i][j]>mm) return 0;
                    if (flag[i][j]==0){flag[i][j]=mm; mark=1;}
                }
            }
        }
        if (mark==0) break;
//printf("%d\n",mark);
//    for (i=1; i<=n; i++) for (j=1; j<=m; j++)
//    printf("%d%c",flag[i][j],j==m ? '\n' : ' ');
    }
    for (i=1; i<=n; i++) for (j=1; j<=m; j++)
        if (flag[i][j]==0) return 0;
    return 1;
}

int main(){
    int i,j,tem,T,cas=0,mark;
freopen("B-large.in","r",stdin);
pout;
    scanf("%d",&T);
    while (T--){
        scanf("%d%d",&n,&m);
        for (i=1; i<=n; i++)
            for (j=1; j<=m; j++)   scanf("%d",&a[i][j]);
        mem(flag,0);
        ans=judge();
        printf("Case #%d: ",++cas);
        if (ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}



























