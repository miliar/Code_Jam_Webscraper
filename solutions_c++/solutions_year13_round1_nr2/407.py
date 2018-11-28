#include <stdio.h>
#include <stdlib.h>

int maxE,r,n,e;
int table[10005];
int m[10005][30];

int min(int a,int b){
    if(a<b){
        return a;
    }
    return b;
}

long long getMax(int n,int e){
    if(m[n][e]!=0){
        return m[n][e];
    }
    for(int i=0;i<=e;i++){
        if(m[n][e] < table[n]*i + getMax(n+1,min(maxE,e-i+r))){
            m[n][e] = table[n]*i + getMax(n+1,min(maxE,e-i+r));
        }
    }
    return m[n][e];
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int i,j;
    int tt,zz;
    scanf("%d",&tt);
    for(zz=1;zz<=tt;zz++){
        scanf("%d%d%d",&e,&r,&n);
        maxE=e;
        for(i=1;i<=n;i++){
            for(j=1;j<=e;j++){
                m[i][j] = 0;
            }
        }
        for(i=1;i<=n;i++){
            scanf("%d",&table[i]);
        }
        for(i=1;i<=e;i++){
            m[n][i] = table[n]*i;
        }
        printf("Case #%d: %lld\n",zz,getMax(1,e));
    }
	return 0;
}
/*
6
5 2 2
2 1
5 2 2
1 2
3 3 4
4 1 3 5
5 2 3
4 1 5
5 3 3
4 1 5
5 2 4
4 3 1 5


last -> 41, 46, 48
*/
