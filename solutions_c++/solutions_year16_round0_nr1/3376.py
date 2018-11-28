#include<iostream>
#include<cstdio>
int main(){
    int t;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++){
        int n;
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",ti);
            continue;
        }
        int ar[10];
        for(int i=0;i<10;i++){
            ar[i]=0;
        }
        int i;
        for(i=n;;i+=n){
            int ii=i;
            while(ii>0){
                ar[ii%10]=1;
                ii/=10;
            }
            int flag=1;
            for(int j=0;j<10;j++){
                if(ar[j]==0){
                    flag=0;
                    break;
                }
            }
            if(flag==1){
                break;
            }
        }
        printf("Case #%d: %d\n",ti,i);
    }
    return 0;
}
