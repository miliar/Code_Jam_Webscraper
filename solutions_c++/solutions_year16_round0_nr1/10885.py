#include<bits/stdc++.h>
using namespace std;

int num,tmp,chk,d,x,p,arr[10]={1,2,4,8,16,32,64,128,256,512};

main(){
    freopen("counting_sheep_output.txt","w",stdout);
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        chk = 0;
        scanf("%d",&tmp);
        if(tmp == 0){
            printf("Case #%d: INSOMNIA\n",i+1);
            continue;
        }
        for(int j=1;;j++){
            p = x = j*tmp;
            while(x!=0){
                d = x%10;
                //printf("%d %d %d\n",arr[d] & chk,x,chk);
                if((arr[d] & chk) == 0)chk += arr[d];
                x /= 10;
            }
            if(chk == 1023){
                printf("Case #%d: %d\n",i+1,p);
                break;
            }
        }
    }
}
