#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int seq(int s,int c,int k,int arr[])
{
if(c==1&&s<k)return -1;
if(c==1){
    for(int i=0;i<k;i++){
        arr[i]=i+1;
    }
    return k;
}
if(k==1){arr[0]=1;return 1;}
for(int i=0;i<k-1;i++){
    arr[i]=i+2;
}
/*
for(int i=0;i<k;i++){
    arr[i]=i+1;
}*/
return k-1;
//return k;
}

int main()
{
int t,res;
int s,c,k,arr[105];
scanf("%d",&t);
for(int i=0;i<t;i++){
scanf("%d%d%d",&k,&c,&s);
res=seq(s,c,k,arr);
if(res==-1){printf("Case #%d: IMPOSSIBLE\n",i+1); continue;}
printf("Case #%d: ",i+1);
for(int i=0;i<res;i++){
    printf("%d ",arr[i]);
 }
 printf("\n");
}

return 0;
}
