#include<iostream>
#include<stdio.h>


int main(){
        
    int t,flips,case_num=1;
    char s[101],top,*x;
    
    scanf("%d",&t);
    while(t-->0){
        
        scanf("%s",s);
        flips = 0;        
        top = s[0];
        x = s;
        while(*x){
            if(*x != top){
                top = *x;
                flips += 1;
            }
            x++;
        }
        if(top == '-'){
            flips+=1;
        }
        printf("Case #%d: %d\n",case_num++,flips);
    }


    return 0;
}
