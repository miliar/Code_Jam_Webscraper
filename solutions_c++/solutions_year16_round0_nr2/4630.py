#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("data1.out","w",stdout);
    int T;
    scanf("%d",&T);
    getchar();
    int j=1;
    while(j<=T){
        char s[101];
        gets(s);
        int dnum=0;
        for(int i=1;i<strlen(s);i++){
            if(s[i]!=s[i-1])
                dnum++;
        }
        if(s[0]=='+'){
            if(dnum%2==0)printf("Case #%d: %d\n",j,dnum);
            else printf("Case #%d: %d\n",j,dnum+1);
        }
        else{
            if(dnum%2==0)printf("Case #%d: %d\n",j,dnum+1);
            else printf("Case #%d: %d\n",j,dnum);
        }
        j++;
    }
}
