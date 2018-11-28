#include <iostream>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
#define Si size()
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;
int n,m;
int a[110][110];

void init(){
    scanf("%d%d",&n,&m);
    for (int i=1;i<=n;++i)
        for (int j=1;j<=m;++j)
            scanf("%d",&a[i][j]);
}

bool work(){
    for (int i=1;i<=n;++i)
        for (int j=1;j<=m;++j){
            bool p=0;
            bool q=0;
            for (int k=1;k<=n;++k)
                if (a[k][j]>a[i][j]) p=1;
            for (int k=1;k<=m;++k)
                if (a[i][k]>a[i][j]) q=1;
            if (p&q) return 0;
        }
    return 1;
}


int main(){
    freopen("bb.in","r",stdin);
    freopen("bb.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int i=1;i<=T;++i){
        printf("Case #%d: ",i);
        init();
        if (work()) printf("YES\n");
            else printf("NO\n");
    }
    return 0;
}
