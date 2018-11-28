#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int Z[1005][1005];
int D[1005][1005], casos, ctos, y, z, b, v;
double A[1005], B[1005];

void din(int x, int y){
    D[x][y]=0;
    Z[x][y]=v;
    int dnde=ctos-y+x;
    if(dnde==ctos){
        if(A[dnde]>B[x])
            D[x][y]=1;
        return ;
    }
    if(A[dnde]>B[x]){
        if(Z[x+1][y]!=v)
            din(x+1, y);
        D[x][y]=D[x+1][y]+1;
    }
    if(A[dnde]<B[y]){
        if(Z[x][y-1]!=v)
            din(x, y-1);
        if(D[x][y-1]>D[x][y])
            D[x][y]=D[x][y-1];
    }
}

int main()
{
    freopen("entrada3.in","r",stdin);
    freopen("salida3.txt","w",stdout);
    scanf("%d",&casos);
    for(v=1; v<=casos; v++){
        scanf("%d",&ctos);
        for(int i=1; i<=ctos; i++)
            scanf("%lf",&A[i]);
        for(int i=1; i<=ctos; i++)
            scanf("%lf",&B[i]);
        sort(A+1, A+ctos+1);
        sort(B+1, B+ctos+1);
        b=1;
        z=0;
        for(int i=1; i<=ctos; i++){
            while(b<=ctos and B[b]<A[i])
                ++b;
            if(b>ctos){
                z=ctos-i+1;
                break;
            }
            ++b;
        }
        din(1, ctos);
        y=D[1][ctos];
        printf("Case #%d: %d %d\n",v,y,z);
    }
    return 0;
}
