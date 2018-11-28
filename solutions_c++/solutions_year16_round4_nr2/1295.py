//#pragma comment(linker,"/STACK:102400000,102400000")
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<time.h>
#include<stdlib.h>
#include<ctype.h>
#include<list>
//#include<ext/rope>
#define PB push_back
#define MP make_pair
#define PF push_front
#define lson k<<1
#define rson k<<1|1
using namespace std;
typedef long long ll;
typedef double db;
typedef long double ldb;

const int N = 1005;
db a[N],b[N],c[N],ans,res;
int n,m;

void calc(int i,int j,db s)
{
    if(i==m)
    {
        ans+=s;
        return;
    }
    if(j<m/2) calc(i+1,j+1,s*b[i]);
    if(i-j<m/2) calc(i+1,j,s*(1.0-b[i]));
}

void dfs(int i,int j)
{
    if(j==m)
    {
        ans=0.0;
        calc(0,0,1.0);
        if(ans>res)
        {
            res=ans;
            for(int k=0; k<m; k++) c[k]=b[k];
        }
        return;
    }
    if(i==n) return;
    dfs(i+1,j);
    b[j]=a[i];
    dfs(i+1,j+1);
}

int main()
{
#ifdef PKWV
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
#endif // PKWV
    int T;
    scanf("%d",&T);
    for(int ca=1; ca<=T; ca++)
    {
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; i++)
        {
            scanf("%lf",&a[i]);
        }
        res=0;
        dfs(0,0);
        printf("Case #%d: %f\n",ca,res);
//    for(int i=0; i<m; i++) printf("%f ",c[i]);
//    printf("\n");
    }
    return 0;
}
