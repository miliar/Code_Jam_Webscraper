#include<iostream>
#include<stdio.h>

int main(){

    int n,cnt[10];
    int i,t,value,case_num=1,sum,temp;
    scanf("%d",&t); 
    while(t-->0){
        scanf("%d",&n);
        value = 0;
        for(i=0;i<10;i++){
            cnt[i] = 0;
        }
        if(n == 0){
            printf("Case #%d: INSOMNIA\n",case_num++);
            continue;
        }
        sum = 0;
        while(sum<10){ // sum = 10 implies all digits found
            value = value + n;
            temp = value;
            //decompose into digits
            while(temp>0){
                cnt[temp%10] = 1;
                temp = temp/10;
            }
            //check if all digits are seen
            sum=0;
            for(i=0;i<10;i++){
                sum=sum+cnt[i];
            }
        }
        printf("Case #%d: %d\n",case_num++,value);
    }
    return 0;
}

