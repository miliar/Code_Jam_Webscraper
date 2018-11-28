#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
typedef long  long ll;

const int N = 105;
const double inf = 1e12;
const double eps = 1e-8;
using namespace std;
int n,m;
int a[N][N];
int r[N],c[N];


bool check(){
    int i,j;
    memset(r,0,sizeof(r));
    memset(c,0,sizeof(c));
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            r[i]=max(r[i],a[i][j]);
            c[j]=max(c[j],a[i][j]);
        }
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            if(a[i][j]<r[i]&&a[i][j]<c[j]) return 0;
        }
    }
    return 1;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        int i,j;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                scanf("%d",&a[i][j]);
            }
        }
        printf("Case #%d: ",cas++);
        if(check()) puts("YES");
        else puts("NO");
    }
    return 0;
}















