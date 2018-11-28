#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int mapview[120][120];
int dir[4][2]={ 1, 0 ,
                -1 , 0,
                0 , 1 ,
                0 , -1 };
int n,m;
int init(){
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;++i)
        for(int j=0;j<m;++j)
            scanf("%d",&mapview[i][j]);
}
int check(int x,int y, int direct){
    int pivot = mapview[x][y];
    int dt1 = dir[direct][0];
    int dt2 = dir[direct][1];
    int u = x;
    int v = y;
    while ( u>=0 && v>=0 && u<n && v<m ){
        if ( mapview[u][v] > pivot )
            return false;
        u += dt1;
        v += dt2;
    }
    return true;
}
int work(){
    for(int i=0;i<n;++i)
        for(int j=0;j<m;++j)
            if (
            ( !check(i,j,0) || !check(i,j,1) ) &&
            ( !check(i,j,2) || !check(i,j,3) )
            ){
                printf("NO\n");
                return 1;
            }
    printf("YES\n");
}
int main(){
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;++i){
        init();
        printf("Case #%d: ",i);
        work();
    }
}
