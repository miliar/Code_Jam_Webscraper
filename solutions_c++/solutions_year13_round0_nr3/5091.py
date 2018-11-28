#include<stdio.h>

int a1[33];

int pal(int a){
    int b=0,n=a;
    while(a!=0){
        b=(b*10)+(a%10);
        a/=10;
    }
    if(n==b)
        return 1;
    else
        return 0;
}

int main(){
    int t,c=0;
    scanf("%d",&t);
    for(int i=1;i<32;i++)
        if(pal(i) && pal(i*i))
            a1[c++]=i*i;
    for(int k=0;k<t;k++){
        int a,b,ans=0;
        scanf("%d %d",&a,&b);
        for(int i=0;i<c;i++){
            if(a1[i]>=a && a1[i]<=b)
                ans++;
            if(a1[i]>b)
                break;
        }
        printf("Case #%d: %d\n",(k+1),ans);
    }
}