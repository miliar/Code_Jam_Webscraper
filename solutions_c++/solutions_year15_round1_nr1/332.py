#include<cstdio>
int bae[100002];
int main(){
    int t,turn,n,i;
    int cal1,cal2,mx=0;
    //freopen("A-large.in-1.txt","r",stdin);
    //freopen("dap.txt","w",stdout);
    scanf("%d",&turn);
    for(t=1;t<=turn;t++){
        scanf("%d",&n);
        cal1=0;cal2=0;mx=0;
        for(i=0;i<n;i++){
            scanf("%d",&bae[i]);
        }
        for(i=1;i<n;i++){
            if(bae[i-1]-bae[i]>0){
                if(bae[i-1]-bae[i]>mx){
                    mx=bae[i-1]-bae[i];
                }
                cal1+=bae[i-1]-bae[i];
            }
        }
        for(i=0;i<n-1;i++){
            if(bae[i]>mx){
                cal2+=mx;
            }else{
                cal2+=bae[i];
            }
        }
        printf("Case #%d: %d %d\n",t,cal1,cal2);
    }
}
