#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int a[105];
char s[105];

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T,ca=0;
    int i,j;
    scanf("%d",&T);
    while(T--){
        ca++;
        scanf("%s",s+1);
        memset(a,0,sizeof(a));
        int len=strlen(s+1);
        for(i=1;i<=len;i++){
            if(s[i]=='+'){
                a[i]=1;
            }
            else{
                a[i]=0;
            }
        }
        int ans=0;
        while(1){
            for(i=2;i<=len;i++){
                if(a[i]!=a[1]) break;
            }
            if(i>len&&a[1]==1) break;
            for(j=1;j<i;j++){
                a[j]=a[j]^1;
            }
            ans++;
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
