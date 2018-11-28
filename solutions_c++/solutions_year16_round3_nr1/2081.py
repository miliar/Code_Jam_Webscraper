#include<stdio.h>

int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        int n;
        scanf("%d",&n);
        int alpha[26]={0};
        for(int j=0;j<n;j++){
            scanf("%d",&alpha[j]);
        }
        printf("Case #%d: ",i);
        while(1){
            int sum=0;
            for(int j=0;j<n;j++){
                sum += alpha[j];
            }
            if(sum==0)
                break;
            int max1=0,max2=0,max1_idx=-1,max2_idx=-1;
            for(int k=0;k<n;k++){
                if(alpha[k]>max2){
                    if(alpha[k]>=max1){
                        max2 = max1;
                        max2_idx = max1_idx;
                        max1 = alpha[k];
                        max1_idx = k;
                    }
                    else{
                        max2 = alpha[k];
                        max2_idx = k;
                    }
                }
            }
            if(max2_idx == -1){
                printf("%c ",max1_idx+'A');
                alpha[max1_idx]--;
            }
            else{
                int p=0;
                alpha[max2_idx]--;
                alpha[max1_idx]--;
                sum-=2;
                for(int j=0;j<n;j++){
                    if((double)((double)alpha[j]/(double)sum) > (double)0.5){
                        p=1;
                        break;
                    }
                }
                if(p==1){
                    alpha[max2_idx]++;
                    printf("%c ",max1_idx+'A');
                }
                else{
                    printf("%c%c ",max1_idx+'A',max2_idx+'A');
                }
            }
        }
        printf("\n");
    }
    return 0;
}