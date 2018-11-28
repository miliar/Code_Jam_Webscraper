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

const int N = 2005;
char res[N],tmp[N];

void calc(int r,int p,int s)
{
    if(r==0) tmp[0]='P',tmp[1]='S';
    else if(p==0) tmp[0]='R',tmp[1]='S';
    else tmp[0]='P',tmp[1]='R';
}

void dfs(int n,int r,int p,int s,int st,int ed)
{
    if(n==1)
    {
        calc(r,p,s);
        res[st]=tmp[0],res[ed]=tmp[1];
        return;
    }
    int mid=(st+ed)/2;
    if(n&1)
    {
        int mx=max(r,max(p,s));
        int d=(mx+1)/2;
        if(r==mx)
        {
            dfs(n-1,d,d-1,d-1,st,mid);
            dfs(n-1,r-d,p-d+1,s-d+1,mid+1,ed);
        }
        else
        {
            dfs(n-1,d-1,d,d-1,st,mid);
            dfs(n-1,r-d+1,p-d,s-d+1,mid+1,ed);
        }
    }
    else
    {
        int mx=max(r,max(p,s));
        int d=mx/2;
        if(r==mx)
        {
            dfs(n-1,d,d,d-1,st,mid);
            dfs(n-1,r-d,p-d,s-d+1,mid+1,ed);
        }
        else
        {
            dfs(n-1,d-1,d,d,st,mid);
            dfs(n-1,r-d+1,p-d,s-d,mid+1,ed);
        }
    }
    bool ok(true);
    for(int i=st; i<=mid; i++) if(res[i]>res[mid+1+i-st])
        {
            ok=false;
            break;
        }
    if(!ok)
    {
        for(int i=st; i<=mid; i++) swap(res[i],res[i-st+mid+1]);
    }
}

vector<int> v[20];

void init()
{
    v[1].PB(0),v[1].PB(1),v[1].PB(1);
    for(int i=2; i<=13; i++)
    {
        for(int j=0; j<3; j++)
            v[i].PB(v[i-1][j]+v[i-1][(j+1)%3]);
        sort(v[i].begin(),v[i].end());
    }
//    for(int i=0;i<3;i++) printf("%d ",v[12][i]);
//    printf("\n");
}

int main()
{
#ifdef PKWV
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
#endif // PKWV
    init();
    int T;
    scanf("%d",&T);
    for(int ca=1; ca<=T; ca++)
    {
        int n;
        int a[4],b[5];
        scanf("%d",&n);
        for(int i=0; i<3; i++) scanf("%d",&a[i]),b[i]=a[i];
        sort(a,a+3);
        bool ok(true);
        for(int i=0; i<3; i++) if(a[i]!=v[n][i]) ok=false;
        printf("Case #%d: ",ca);
        if(ok)
        {
            dfs(n,b[0],b[1],b[2],0,(1<<n)-1);
            res[(1<<n)]=0;
            printf("%s",res);
        }
        else printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
