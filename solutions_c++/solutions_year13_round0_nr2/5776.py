#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    for(int k=0;k<t;k++){
        int n,m,flag1=0,flag2=0,flag3=0;
        scanf("%d %d", &n, &m);
        int a[n][m];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        
        for(int i=0;i<n;i++){
            flag1=0;flag2=0;
            for(int j=0;j<m;j++){
                if(a[i][j]==1){
                    for(int l=0;l<n;l++)
                        if(a[l][j]==2)
                            flag1=1;
                    for(int l=0;l<m;l++)
                        if(a[i][l]==2)
                            flag2=1;
                }
            }
            if(flag1 && flag2){
                flag3=1;
                break;
            }
        }
        if(flag3)
            printf("Case #%d: NO\n",(k+1));
        else
            printf("Case #%d: YES\n",(k+1));
    }
}