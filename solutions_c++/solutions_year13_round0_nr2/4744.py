#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <string.h>
#include <queue>
#include <map>
#include <set>
#include <math.h>
#include <sstream>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;

const int dx[8]={1,0,-1,0,-1,-1,1,1};
const int dy[8]={0,1,0,-1,1,-1,1,-1};
const int days[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
const int leap[13]={0,31,29,31,30,31,30,31,31,30,31,30,31};

int a[111][111];
bool b1[111][111],b2[111][111];
int n,m;

void wk(int p,int q,int k,int xx,int yy,int l){
    for (int i=0;i<l;++i)
        if (a[p+xx*i][q+yy*i]>k) return;
    for (int i=0;i<l;++i)
        if (a[p+xx*i][q+yy*i]==k) b2[p+xx*i][q+yy*i]=true;
}

void work(int p,int q,int k){
    if (p==0) wk(p,q,k,1,0,n);
    if (p==n-1) wk(p,q,k,-1,0,n);
    if (q==0) wk(p,q,k,0,1,m);
    if (q==m-1) wk(p,q,k,0,-1,m);
}

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;++i)
            for (int j=0;j<m;++j)
                scanf("%d",&a[i][j]);
        memset(b1,true,sizeof(b1));
        memset(b2,false,sizeof(b2));
        for (int k=100;k>=0;--k){
            memset(b1,true,sizeof(b1));            
            for (int i=0;i<n;++i)
                for (int j=0;j<m;++j)
                    if ((i==0 || i==n-1 || j==0 || j==m-1) && a[i][j]<=k && b1[i][j]) work(i,j,k);
        }
        bool ans=true;
        for (int i=0;i<n;++i)
            for (int j=0;j<m;++j)
                ans&=b2[i][j];
        printf("Case #%d: %s\n",++cas,ans?"YES":"NO");
    }
    return 0;
}
