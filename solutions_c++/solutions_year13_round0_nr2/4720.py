#include <iostream>
#include <cstdio>
#include <cctype>
#include<algorithm>
#include<cstring>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))

const int N = 110;

int a[N][N];
int mxr[N];
int mxc[N];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.ou","w",stdout);

    int T; scanf("%d",&T);
    for(int ka=1;ka<=T;ka++) {
        mem(mxr,0);mem(mxc,0);
        int n,m; scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) {
            scanf("%d",&a[i][j]);
            mxr[i]=max(mxr[i],a[i][j]);
            mxc[j]=max(mxc[j],a[i][j]);
        }
        int ok=1;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) {
            if(a[i][j]==min(mxr[i],mxc[j])) continue;
            ok=0;
            break;
        }
        printf("Case #%d: %s\n",ka,ok?"YES":"NO");
    }

    return 0;
}
