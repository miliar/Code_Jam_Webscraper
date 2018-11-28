#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main() {
    freopen("PancakesIn.txt","r",stdin);
    freopen("PancakesOut.txt","w",stdout);
    int T,N,i,k,count,l,flag;
    char S[102];
    scanf("%d",&T);
    for(k=1;k<=T;k++) {
        scanf("%s",S);
        l=strlen(S);
        flag=0;
        count=0;
        for(i=l-1;i>=0;i--) {
            if(flag==0) {
                if(S[i]=='-') {
                    count++;
                    flag=1;
                    continue;
                }
            } else {
                if(S[i]=='+') {
                    count++;
                    flag=0;
                }
            }
        }
        printf("Case #%d: %d\n",k,count);
    }
    return 0;
}
