#include<bits/stdc++.h>
using namespace std;

int main(){

FILE *fin,*fout;
fin=freopen("A-large.in","r",stdin);
fout=freopen("output1.txt","w+",stdout);

int t;
int z;
scanf("%d",&t);
z=t;
while(t--){

int arr[10];
for(int i=0;i<10;i++){
arr[i]=0;
}
long long in;
scanf("%lld",&in);
if(in==0){
printf("Case #%d: INSOMNIA\n",z-t);
goto dont;
}
long long temp,flag,mul;
flag=0;
mul=1;
re: temp=in*mul;
flag=0;
while(temp>0)
{
int x=temp%10;
//printf("%d",x);
arr[x]=1;
temp=temp/10;
}
for(int i=0;i<10;i++){
if(arr[i]==0)
flag=1;
}
if(flag==1){
mul++;
goto re;
}
printf("Case #%d: %lld\n",z-t,in*mul);

dont: ;
}

fclose(fout);
fclose(fin);
return 0;
}
