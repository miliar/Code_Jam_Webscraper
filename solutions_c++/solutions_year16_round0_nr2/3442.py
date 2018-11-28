#include<iostream>
#include<cstdio>
int main(){
    int t;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++){
        char s[1100];
        scanf("%s",s);
        int n=0;
        for(int i=1;s[i]!='\0';i++){
            if(s[i]!=s[i-1]){
                n++;
            }
        }
        if((n%2==0 && s[0]=='+')||(n%2==1 && s[0]=='-')){
            printf("Case #%d: %d\n",ti,n);
        }
        else{
            printf("Case #%d: %d\n",ti,n+1);
        }
    }
    return 0;
}
