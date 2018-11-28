#include<stdio.h>

int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        int n,check[10]={0},j;
        scanf("%d",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",i);
        else{
            for(j=1;;j++){
                int num = n*j;
                while(1){
                    if(num==0) break;
                    check[num%10]=1;
                    num/=10;
                }
                int sum=0;
                for(int k=0;k<=9;k++){
                    if(check[k])
                        sum++;
                }
                if(sum == 10)
                    break;
            }
            printf("Case #%d: %d\n",i,j*n);
        }
    }
    return 0;
}