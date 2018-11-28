#include<iostream>
#include<stdio.h>
#include<cmath>
#include<fstream>
using namespace std;
int main(){
   freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
long long int t,a,b,test,j,k,min,max,index1,index2,ans,flag,flag1;
long long int arr[48]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL,100220141022001LL,102012040210201LL,102234363432201LL,121000242000121LL,121242363242121LL,123212464212321LL,123456787654321LL,400000080000004LL};
/*for(int i=0;i<48;i++)
{
    printf("%lld\n",arr[i]);
}*/
scanf("%lld",&t);
for(test=1;test<=t;test++){
    flag=0;
    flag1=0;
scanf("%lld",&a);
scanf("%lld",&b);
min=1;
max=1;
for(j=0;j<48;j++){
if(arr[j]>=a){
index1=j;
flag=1;
break;
}}
if(flag==0){
index1=48;
}
for(j=0;j<48;j++){
if(arr[j]<=b){
index2=j;
}
}
ans=index2-index1+1;
printf("Case #%lld: %lld\n",test,ans);
}

return 0;
}

