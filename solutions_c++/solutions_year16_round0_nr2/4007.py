#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int abs(int a){
    return a>0?a:-a;
}

char s[1000];
int main(){
    int n,m,a,T,icas=0;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%s",s);
        n=strlen(s);
        for(int i=0;i<n;++i){
            if(s[i]=='-')
                s[i]=1;
            else s[i]=0;
        }
        int sum=0,p=0;
        for(int i=n-1;i>=0;--i){
            if(s[i]^p==1){
                sum++;
                p^=1;
            }
        }
        printf("Case #%d: %d\n",++icas,sum);
    }
    return 0;
}
