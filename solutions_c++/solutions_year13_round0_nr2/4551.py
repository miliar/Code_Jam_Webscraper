#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
int a[1024][1024];
int n, m;
bool checkcol(int r, int c){
    int i;
    for(i=0;i<n;i++)
        if(a[i][c] > a[r][c])
            return 0;
    return 1;
}

bool checkrow(int r, int c){
    int i;
    for(i=0;i<m;i++)
        if(a[r][i] > a[r][c]){
            return 0;
        }
    return 1;
}
int main(){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#else
    freopen("tetrahedron.in", "r", stdin);
    freopen("tetrahedron.out", "w", stdout);
#endif
    int i, j;
    int T, Tests;
    scanf("%d",&Tests);
    for(T=1;T<=Tests;T++){
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                scanf("%d",a[i]+j);
        bool p=0;
        for(i=0;i<n && !p;i++)
            for(j=0;j<m && !p;j++)
                if((p=(!checkcol(i,j) && !checkrow(i,j))))
                    printf("Case #%d: NO\n", T, i, j);
        if(!p)
            printf("Case #%d: YES\n", T);
     }


    return 0;
}
