#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
typedef unsigned long long  LL;
using namespace std ;
typedef pair<int,int> PII;

int main(){
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int k,_;
    scanf("%d",&_);
    for (k=1;k<=_;k++){
        int x,y,i,j,a[10][10],b[10][10];
        scanf("%d",&x);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        int ans,cnt=0;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++)
                if (a[x][i]==b[y][j]){
                    ++cnt; ans=a[x][i];
                }
        printf("Case #%d: ",k);
        if (cnt==1) printf("%d\n",ans);
        else if (cnt==0) puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
}

