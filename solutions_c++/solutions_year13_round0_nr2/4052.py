#include<stdio.h>

struct lwn {
    int a,b;
};

int vali(int arr[][110],int i,int j, int n, int m)
{
    int l,x=0;
    for(l=0; l<n; l++) {
        if(arr[l][j]>arr[i][j]) {
            x=1;
            break;
        }
    }
    if(x==1) {
        for(l=0; l<m; l++) {
            if(arr[i][l]>arr[i][j])
                return 1;
        }
    }
    return 0;
}
int main()
{
    int cas , t=1;
    scanf("%d",&cas);
    while(t<=cas) {
        int n,m,i,j,arr[110][110],flag=0;
        scanf("%d%d",&n,&m);
        for(i=0; i<n; i++) {
            for(j=0; j<m; j++)
                scanf("%d",&arr[i][j]);
        }
        for(i=0; i<n; i++) {
            for(j=0; j<m; j++) {
                if(vali(arr,i,j,n,m)==1) {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
                break;
        }
        if(flag!=1)
            printf("Case #%d: YES\n",t);
        else
            printf("Case #%d: NO\n",t);
        t++;
    }
    return 0;
}
