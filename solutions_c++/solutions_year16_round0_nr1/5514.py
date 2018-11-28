#include <cstdio>



int main (){
    int T;
    scanf("%d",&T);
    for(int I= 1 ; I <= T ; I ++){
        bool num[10]={0};
        int cnt=0;
        int x;
        scanf("%d",&x);
        if(x==0){
            printf("Case #%d: INSOMNIA\n",I);
            continue;
        }
        int i;
        for(i = 1 ; cnt!= 10 ; i++ ){
            int n=i*x;
            for(;n>0&&cnt!=10;n/=10){
                if(!num[n%10]){
                    num[n%10]=true;
                    cnt++;
                }
            }
        }
        i--;
        printf("Case #%d: %d\n",I,i*x);

    }

}
