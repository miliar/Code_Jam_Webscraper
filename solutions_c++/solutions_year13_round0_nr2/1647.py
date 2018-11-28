#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<string>
using namespace std;
const int N=100+10;
int n,m;
int a[N][N];
int x[N],y[N];
bool check(){
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (a[i][j]<x[i] && a[i][j]<y[j]) return 0;
        }
    }
    return 1;
}
int main(){
    int T,cas=0;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        memset(x,0,sizeof(x));
        memset(y,0,sizeof(y));
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                scanf("%d",&a[i][j]);
                x[i]=max(x[i],a[i][j]);
                y[j]=max(y[j],a[i][j]);
            }
        }
        printf("Case #%d: ",++cas);
        if (check()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
