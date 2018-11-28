#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int k,c,s,t;
int main()
{
//freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
scanf("%d",&t);
for(int tt=1;tt<=t;tt++){
scanf("%d %d %d",&k,&c,&s);
   printf("Case #%d: ",tt);
if(c==1){
if(s>=k){
    for(int i=0;i<k;i++){
        if(i){
            printf(" ");}
        printf("%d",i+1);}
    printf("\n");}else{
printf("IMPOSSIBLE\n");
}}else{
if(s>=(k-1)){
if(k==1){printf("1\n");}else{
    long long pos=2;
    for(int i=1;i<k;i++){
        if(i>1){printf(" ");}
        printf("%lld",pos);
        pos+=k+1;
    }
    printf("\n");
    }}else{
printf("IMPOSSIBLE\n");
}}}

    return 0;
}
