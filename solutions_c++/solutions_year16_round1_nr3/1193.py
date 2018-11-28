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
int M[1003];
bool f[1003];
int n,m;
int ans,ans1,ans2;
void DFS(int x,int q,int k)
{
    //pri("%d ",x);
    if (M[x]==m){
        ans=max(ans,k);
    }
    f[x]=1;
    if (M[x]==q)
    {
        ans=max(ans,k);
        for (int i=1;i<=n;i++)
        if (!f[i]){
            DFS(i,x,k+1);
        }
    }
    else
    {
        if (f[M[x] ]==1 )
        {
            f[x]=0;
            return ;
        }
        else
        {
            DFS(M[x],x,k+1);
        }
    }
    f[x]=0;
    return ;
}


int main(){
    int i,j;
    int T;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C.out","w",stdout);
    sca("%d",&T);
    for (int cas=1;cas<=T;cas++){
        sca("%d",&n);
        for (i=1;i<=n;i++){
            sca("%d",&M[i]);
            f[i]=0;
        }
        ans=ans1=ans2=0;
        for (m=1;m<=n;m++)
        {
            f[m]=1;
           // pri("%d ",m);
            DFS(M[m],m,2);
            f[m]=0;
           // pri("\n");
        }
        pri("Case #%d: %d\n",cas,ans);
    }
    return 0;
}





















