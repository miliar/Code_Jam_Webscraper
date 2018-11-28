#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool ispalindrome(int n){
    char s[10];
    sprintf(s,"%d",n);
    int l = strlen(s);
    for(int a=0,b=l-1; a<=b; a++,b--)
        if(s[a]!=s[b])return 0;
        
    return 1;
}

int main(){
    bool pal[1100]={};
    for(int i=0; i*i <= 1100; i++){
        if(ispalindrome(i) && ispalindrome(i*i))
            pal[i*i]=1;
    } 
    
    int _test;
    scanf("%d",&_test);
    for(int tc=1;tc<=_test;tc++){
        int a,b;
        scanf("%d %d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;i++)
            ans+=pal[i];
        printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}
