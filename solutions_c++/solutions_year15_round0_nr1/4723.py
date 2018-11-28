#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int T,I;
    scanf("%d",&T);
    for(I=0;I<T;I++){
        int n,ans=0,now=0,i,j;
        char s[2000];
        scanf("%d %s",&n,s);
        for(i=0;i<=n;i++){
            int m=s[i]-'0';
            if(now<i){
                ans+=(i-now);
                now=i;
            }
            now+=m;
        }
        printf("Case #%d: %d\n",I+1,ans);
    }
}