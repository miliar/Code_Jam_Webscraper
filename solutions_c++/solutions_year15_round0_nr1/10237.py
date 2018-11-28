#include<stdio.h>
#include<fstream>
int main(){
    freopen("A-small-attempt2.in","r",stdin);
freopen("A-small-attempt2.out","w",stdout);
int T=0;
scanf("%d",&T);
int S=0,invite=0,sum=0;
int A[1001];
for(int i=1;i<=T;i++){
        sum=0;
        invite=0;
    scanf("%d",&S);
    for(int j=0;j<=S;j++){
        scanf("%1d",&A[j]);
        if(j>0){
            sum+=A[j-1];
            if(sum<j)
            {
                invite+=j-sum;
                sum+=1;
            }
        }
    }
    printf("Case #%d: %d\n",i,invite);

}
}
