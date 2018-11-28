#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main() {
    //freopen("Digits.txt","r",stdin);
    freopen("A-small-attempt0.txt","r",stdin);
    freopen("DigitsOutput.txt","w",stdout);
    int T,i,j,k,len;
    char S[2002],hash[27],dig[11];
    scanf("%d",&T);
    for(k=1;k<=T;k++) {
        for(i=0;i<27;i++) {
            hash[i]=0;
        }
        for(i=0;i<11;i++) {
            dig[i]=0;
        }
        scanf("%s",S);
        len=strlen(S);
        for(i=0;i<len;i++) {
            hash[S[i]-64]++;
        }
        while(hash[7]!=0){
            dig[8]++;
            hash[5]--;
            hash[9]--;
            hash[7]--;
            hash[8]--;
            hash[20]--;
        }
        while(hash[21]!=0){
            dig[4]++;
            hash[6]--;
            hash[15]--;
            hash[21]--;
            hash[18]--;
        }
        while(hash[23]!=0){
            dig[2]++;
            hash[20]--;
            hash[23]--;
            hash[15]--;
        }
        while(hash[24]!=0){
            dig[6]++;
            hash[19]--;
            hash[9]--;
            hash[24]--;
        }
        while(hash[26]!=0){
            dig[0]++;
            hash[26]--;
            hash[5]--;
            hash[18]--;
            hash[15]--;
        }
        while(hash[19]!=0){
            dig[7]++;
            hash[19]--;
            hash[5]--;
            hash[22]--;
            hash[5]--;
            hash[14]--;
        }
        while(hash[6]!=0){
            dig[5]++;
            hash[6]--;
            hash[9]--;
            hash[22]--;
            hash[5]--;
        }
        while(hash[20]!=0){
            dig[3]++;
            hash[20]--;
            hash[8]--;
            hash[18]--;
            hash[5]--;
            hash[5]--;
        }
        while(hash[15]!=0){
            dig[1]++;
            hash[15]--;
            hash[14]--;
            hash[5]--;
        }
        while(hash[14]!=0){
            dig[9]++;
            hash[14]--;
            hash[9]--;
            hash[14]--;
            hash[5]--;
        }
        printf("Case #%d: ",k);
        for(i=0;i<10;i++){
            while(dig[i]!=0){
                printf("%d",i);
                dig[i]--;
            }
        }
        printf("\n");
    }
    return 0;
}
