#include <stdio.h>
int h[2505];
int tc;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("Boutput.txt","w",stdout);
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        for(int i=0;i<2505;i++){
            h[i]=0;
        }
        int n,w;
        scanf("%d",&n);
        for(int i=0;i<2*n-1;i++){
            for(int j=0;j<n;j++){
                scanf("%d",&w);
                h[w]++;
            }
        }
        printf("Case #%d: ",t);
        for(int i=0;i<=2500;i++){
            if(h[i]%2==1){
                printf("%d ",i);
            }
        }
        printf("\n");
    }
}
