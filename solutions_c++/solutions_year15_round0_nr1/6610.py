#include<stdio.h>
#include<iostream>
using namespace std ;
int main()
{
    long long t ,i,c,s,m ,k,p=1;
    char a[1001] ;
    scanf("%lld",&t) ;
    while(t--){
        scanf("%lld",&m);
        scanf("%s",a) ;
        s=(long long)(a[0]-48) ;
        c=0 ;
        for(i=1;a[i]!='\0';i++){

            if(i>s){
                    k=i-s;
                c=c+k ;

                s=s+k+(long long)(a[i]-48) ;
            }
            else{
                s=s+(long long)(a[i]-48) ;
            }
        }
        printf("Case #%lld: %lld\n",p,c);
        p++;
    }
    return 0 ;
}
