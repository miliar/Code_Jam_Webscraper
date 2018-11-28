#include<stdio.h>
int main(){
    int T;
    int N,tmp1,tmp2;
    int arr[10],sum,ccount=0;
    scanf("%d",&T);
   // N=999900-1;
    while(T--){
        ccount++;
        for(int i=0;i<10;i++) arr[i]=0;
        //N++;
        scanf("%d",&N);
        sum=tmp1=0;
        if(N==0)
            printf("Case #%d: INSOMNIA\n",ccount);
        else{
            while(sum<10){
                tmp1+=N;
                tmp2=tmp1;
                while(tmp2>0){
                    if(arr[tmp2%10]==0){
                        arr[tmp2%10]=1;
                        sum++;
                    }
                    tmp2/=10;
                    if(sum==10){
                        printf("Case #%d: %d\n",ccount,tmp1);
                        break;
                    }
                }
            }

        }

    }
    return 0;
}
